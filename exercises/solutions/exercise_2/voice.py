
from __future__ import annotations

import os
import uuid
import json
import asyncio
import base64
import logging
import threading
import numpy as np
import sounddevice as sd

from dotenv import load_dotenv
from typing import Dict, Union, Literal, Optional, Set, Callable, Awaitable
from typing_extensions import AsyncIterator, TypedDict, Required
from websockets.asyncio.client import connect as ws_connect
from websockets.asyncio.client import ClientConnection as AsyncWebsocket
from websockets.asyncio.client import HeadersLike
from websockets.typing import Data
from websockets.exceptions import WebSocketException
from azure.identity import DefaultAzureCredential
from azure.core.credentials_async import AsyncTokenCredential
from azure.identity import DefaultAzureCredential

logger = logging.getLogger(__name__)
AUDIO_SAMPLE_RATE = 24000

AudioTimestampTypes = Literal["word"]

class AzureDeepNoiseSuppression(TypedDict, total=False):
    type: Literal["azure_deep_noise_suppression"]

class ServerEchoCancellation(TypedDict, total=False):
    type: Literal["server_echo_cancellation"]

class AzureSemanticDetection(TypedDict, total=False):
    model: Literal["semantic_detection_v1"]
    threshold: float
    timeout: float

EOUDetection = AzureSemanticDetection

class AzureSemanticVAD(TypedDict, total=False):
    type: Literal["azure_semantic_vad"]
    end_of_utterance_detection: EOUDetection
    threshold: float
    silence_duration_ms: int
    prefix_padding_ms: int

class Animation(TypedDict, total=False):
    outputs: Set[Literal["blendshapes", "viseme_id", "emotion"]]

class Session(TypedDict, total=False):
    voice: Dict[str, Union[str, float]]
    turn_detection: Union[AzureSemanticVAD]
    input_audio_noise_reduction: AzureDeepNoiseSuppression
    input_audio_echo_cancellation: ServerEchoCancellation
    animation: Animation
    output_audio_timestamp_types: Set[AudioTimestampTypes]

class SessionUpdateEventParam(TypedDict, total=False):
    type: Literal["session.update"]
    session: Required[Session]
    event_id: str

class AsyncVoiceLiveSessionResource:
    def __init__(self, connection: AsyncVoiceLiveConnection) -> None:
        self._connection = connection

    async def update(
        self,
        *,
        session: Session,
        event_id: str | None = None,
    ) -> None:
        param: SessionUpdateEventParam = {
            "type": "session.update", "session": session, "event_id": event_id
        }
        data = json.dumps(param)
        await self._connection.send(data)

class AsyncVoiceLiveConnection:
    session: AsyncVoiceLiveSessionResource
    _connection: AsyncWebsocket

    def __init__(self, url: str, additional_headers: HeadersLike) -> None:
        self._url = url
        self._additional_headers = additional_headers
        self._connection = None
        self.session = AsyncVoiceLiveSessionResource(self)

    async def __aenter__(self) -> AsyncVoiceLiveConnection:
        try:
            self._connection = await ws_connect(self._url, additional_headers=self._additional_headers)
        except WebSocketException as e:
            raise ValueError(f"Failed to establish a WebSocket connection: {e}")
        return self

    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        if self._connection:
            await self._connection.close()
            self._connection = None
    
    enter = __aenter__
    close = __aexit__

    async def __aiter__(self) -> AsyncIterator[Data]:
        async for data in self._connection:
            yield data

    async def recv(self) -> Data:
        return await self._connection.recv()
    
    async def recv_bytes(self) -> bytes:
        return await self._connection.recv()

    async def send(self, message: Data) -> None:
        await self._connection.send(message)


class AsyncAzureVoiceLive:
    def __init__(
        self,
        *,
        azure_endpoint: str | None = None,
        api_version: str | None = "2025-05-01-preview",
        api_key: str | None = None,
        azure_ad_token_credential: AsyncTokenCredential | None = None,
        foundry_credential: AsyncTokenCredential | None = None,
        project_name: str | None = None,
        agent_id: str | None = None,
    ) -> None:
        if azure_endpoint is None:
            azure_endpoint = os.environ.get("AZURE_VOICE_LIVE_ENDPOINT")

        if azure_endpoint is None:
            raise ValueError(
                "Must provide the 'azure_endpoint' argument, or the 'AZURE_VOICE_LIVE_ENDPOINT' environment variable"
            )

        if api_key is None and azure_ad_token_credential is None:
            api_key = os.environ.get("AZURE_VOICE_LIVE_API_KEY")

        if api_key is None and azure_ad_token_credential is None:
            raise ValueError(
                "Missing credentials. Please pass one of 'api_key', 'azure_ad_token_credential', or the 'AZURE_VOICE_LIVE_API_KEY' environment variable."
            )

        if api_key and azure_ad_token_credential:
            raise ValueError(
                "Duplicating credentials. Please pass one of 'api_key' and 'azure_ad_token_credential'"
            )

        self._api_key = api_key
        self._azure_endpoint = azure_endpoint
        self._project_name = project_name
        self._agent_id = agent_id
        self._api_version = api_version
        self._azure_ad_token_credential = azure_ad_token_credential
        self._foundry_credential = foundry_credential
        self._connection = None
        self._token = self.get_token() if azure_ad_token_credential else None
        self._foundry_token = self.get_foundry_token() if foundry_credential else None

    def get_token(self) -> str:
        if self._azure_ad_token_credential:
            scopes = "https://ai.azure.com/.default"
            token = self._azure_ad_token_credential.get_token(scopes)
            return token.token
        else:
            return None
        
    def get_foundry_token(self) -> str:
        if self._foundry_credential:
            scopes = "https://ai.azure.com/.default"
            token = self._foundry_credential.get_token(scopes)
            return token.token
        else:
            return None        

    def refresh_token(self) -> None:
        self._token = self.get_token()

    def connect(self, model: str, agent_id: str = None) -> AsyncVoiceLiveConnection:
        if self._connection is not None:
            raise ValueError("Already connected to the Azure Voice Agent service.")
        if not model:
            raise ValueError("Model name is required.")
        if not isinstance(model, str):
            raise TypeError(f"The 'model' parameter must be of type 'str', but got {type(model).__name__}.")


        request_id = uuid.uuid4()

        url = f"{self._azure_endpoint.rstrip('/')}/voice-agent/realtime?api-version={self._api_version}&model={model}&agent_id={agent_id or self._agent_id}&agent-project-name={self._project_name}&agent_access_token={self._foundry_token}&Authorization=Bearer+{self._token}"
        url = url.replace("https://", "wss://")
        # print(f"Connecting to Azure Voice Agent at {url}")

        auth_header = {"Authorization": f"Bearer {self._token}"} if self._token else {"api-key": self._api_key}        
        headers = {"x-ms-client-request-id": str(request_id), **auth_header}

        self._connection = AsyncVoiceLiveConnection(
            url,
            additional_headers=headers,
        )
        return self._connection


# --- End of Embedded Code ---

class AudioPlayerAsync:
    def __init__(self):
        self.queue = []
        self.lock = threading.Lock()
        self.stream = sd.OutputStream(
            callback=self.callback,
            samplerate=AUDIO_SAMPLE_RATE,
            channels=1,
            dtype=np.int16,
            blocksize=1200,
        )
        self.playing = False

    def callback(self, outdata, frames, time, status):
        with self.lock:
            data = np.empty(0, dtype=np.int16)
            while len(data) < frames and len(self.queue) > 0:
                item = self.queue.pop(0)
                frames_needed = frames - len(data)
                data = np.concatenate((data, item[:frames_needed]))
                if len(item) > frames_needed:
                    self.queue.insert(0, item[frames_needed:])
            if len(data) < frames:
                data = np.concatenate((data, np.zeros(frames - len(data), dtype=np.int16)))
        outdata[:] = data.reshape(-1, 1)

    def add_data(self, data: bytes):
        with self.lock:
            np_data = np.frombuffer(data, dtype=np.int16)
            self.queue.append(np_data)
            if not self.playing:
                self.start()

    def start(self):
        self.playing = True
        self.stream.start()

    def stop(self):
        with self.lock:
            self.queue = []
        self.playing = False
        self.stream.stop()

    def terminate(self):
        self.stream.close()

async def listen_and_send_audio(connection: AsyncVoiceLiveConnection) -> None:
    logger.info("Starting audio stream ...")

    stream = sd.InputStream(channels=1, samplerate=AUDIO_SAMPLE_RATE, dtype="int16")
    try:
        stream.start()
        read_size = int(AUDIO_SAMPLE_RATE * 0.02)
        while True:
            if stream.read_available < read_size:
                continue
            data, _ = stream.read(read_size)
            audio = base64.b64encode(data).decode("utf-8")
            param = {"type": "input_audio_buffer.append", "audio": audio, "event_id": ""}
            data_json = json.dumps(param)
            try:
                await connection.send(data_json)
            except (ConnectionResetError, WebSocketException) as e:
                logger.error(f"WebSocket error while sending audio: {e}")
                break
    except Exception as e:
        logger.debug(f"Audio stream interrupted. {e}")
    finally:
        stream.stop()
        stream.close()
        logger.info("Audio stream closed.")



async def receive_audio_and_playback(connection: AsyncVoiceLiveConnection) -> None:
    last_audio_item_id = None
    audio_player = AudioPlayerAsync()

    logger.info("Starting audio playback ...")
    try:
        while True:
            transcript = ""
            async for raw_event in connection:
                try:
                    event = json.loads(raw_event)
                except json.JSONDecodeError as e:
                    logger.error(f"Failed to decode event: {e}")
                    break

                if event.get("type") == "response.audio.delta":
                    if event.get("item_id") != last_audio_item_id:
                        last_audio_item_id = event.get("item_id")
                    bytes_data = base64.b64decode(event.get("delta", ""))
                    audio_player.add_data(bytes_data)
                elif event.get("type") == "response.audio_transcript.done":
                    transcript = event.get("transcript", "")
                    print(f"Final Transcript: {transcript}")
                elif event.get("type") == "conversation.item.created":
                    item = event.get("item", None)
                    if item is not None:
                        content = item.get("content", [])
                        if len(content) > 0:
                            for c in content:
                                if item.get("role", "") == "user":
                                    print(f"User Transcript: {c.get('transcript', '')}")

                elif event.get("type") == "response.done":                    
                    break
    except (ConnectionResetError, WebSocketException) as e:
        logger.error(f"WebSocket error in audio playback: {e}")
    except Exception as e:
        logger.error(f"Error in audio playback: {e}")
    finally:
        audio_player.terminate()
        logger.info("Playback done.")

async def read_keyboard_and_quit() -> None:
    print("Press 'q' and Enter to quit the chat.")
    while True:
        # Run input() in a thread to avoid blocking the event loop
        user_input = await asyncio.to_thread(input) 
        if user_input.strip().lower() == 'q':
            print("Quitting the chat...")
            break




class AgentVoice():

    def __init__(self, 
                agent_id: str = None, 
                project_name: str = None,
                endpoint: str = None,
                deployment: str = None,
                api_key: str = None
            ) -> None:
        
        self.agent_id = agent_id or os.environ.get("AZURE_VOICE_LIVE_AGENT_ID") 
        self.project_name = project_name or os.environ.get("AZURE_FOUNDRY_PROJECT_NAME") 

        self.endpoint = endpoint or os.environ.get("AZURE_VOICE_LIVE_ENDPOINT")
        self.deployment = deployment or os.environ.get("AZURE_VOICE_LIVE_DEPLOYMENT")
        self.api_key = api_key or os.environ.get("AZURE_VOICE_LIVE_API_KEY")
        print(f"Using agent_id: {self.agent_id}")

        if not self.endpoint or not self.deployment:
            raise ValueError("Both AZURE_VOICE_LIVE_ENDPOINT and AZURE_VOICE_LIVE_DEPLOYMENT environment variables must be set.")
    

    def __repr__(self) -> str:
        return f"AgentVoice(agent_id={self.agent_id}, project_name={self.project_name})"

    async def connect(self) -> None:
        client = AsyncAzureVoiceLive(
            azure_endpoint = self.endpoint,
            # api_key = self.api_key,
            azure_ad_token_credential=DefaultAzureCredential(),
            foundry_credential=DefaultAzureCredential(),
            project_name = self.project_name,
            agent_id = self.agent_id,
        )

        async with client.connect(model = self.deployment) as connection:
            await connection.session.update(
                session={
                    "turn_detection": {
                        "create_response": True,
                        "interrupt_response": True,
                        "type": "azure_semantic_vad",
                        "threshold": 0.5,
                        "prefix_padding_ms": 400,
                        "silence_duration_ms": 400,
                        "remove_filler_words": True,
                        "end_of_utterance_detection": {
                            "model": "semantic_detection_v1",
                            "threshold": 0.01,
                            "timeout": 3,
                        },
                    },
                    "input_audio_transcription": {"model": "azure-fast-transcription"},     
                    "input_audio_noise_reduction": {"type": "azure_deep_noise_suppression"},
                    "input_audio_echo_cancellation": {"type": "server_echo_cancellation"},
                    "voice": {
                        "name": "en-US-Aria:DragonHDLatestNeural",
                        "type": "azure-standard",
                        "temperature": 0.3,
                    },      
                    # "model": "gpt-4.1",
                    "modalities": ["audio", "text"],
                    "tool_choice": "auto",
                    # "agent":{
                    #     "type": "agent",
                    #     "name": "test_research_agent",
                    #     "description": "Research agent for testing purposes",
                    #     "agent_id": agent_id,
                    #     "thread_id": ""
                    # }
                }
            )

            send_task = asyncio.create_task(listen_and_send_audio(connection))
            receive_task = asyncio.create_task(receive_audio_and_playback(connection))
            keyboard_task = asyncio.create_task(read_keyboard_and_quit())

            print("Starting the chat ...")
            await asyncio.wait([send_task, receive_task, keyboard_task], return_when=asyncio.FIRST_COMPLETED)

            send_task.cancel()
            receive_task.cancel()
        print("Chat done.")

if __name__ == "__main__":
    try:
        load_dotenv()
        av = AgentVoice(agent_id="asst_bEgFu4ATuu5XvMjHBP3y85ac")
        asyncio.run(av.connect())
    except Exception as e:
        print(f"Error: {e}")
        