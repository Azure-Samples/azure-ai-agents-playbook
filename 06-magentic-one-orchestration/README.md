# Magentic-One Orchestration

Learn advanced multi-agent orchestration using the Magentic-One framework. Build sophisticated agent systems that coordinate multiple specialists for complex workflows like creative content generation and research automation.

## What You'll Learn

- Master the Magentic-One framework for agent orchestration
- Build systems where agents collaborate intelligently
- Create creative content pipelines and research workflows
- Implement feedback loops and quality assessment
- Automate comprehensive web research with verification

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Magentic-One Orchestrator                    │
│                  (StandardMagenticManager)                      │
└─────────────────────┬───────────────────────────────────────────┘
                      │
    ┌─────────────────┼─────────────────┬─────────────────┐
    │                 │                 │                 │
┌───▼────┐    ┌──────▼──────┐    ┌─────▼─────┐    ┌─────▼─────┐
│Creative│    │  Research   │    │   Fact    │    │  Report   │
│ Agent  │    │   Agent     │    │  Checker  │    │Generator  │
└────────┘    └─────────────┘    └───────────┘    └───────────┘
```

![SK Orchestration](images/sk_orchestration.gif)

## Tutorials

**[06.1 - Creative Writing Pipeline](06.1-magentic_creative_writing_tutorial.ipynb)**
Multi-agent creative content system with joke writers, haiku converters, and translators. Learn feedback loops and quality assessment.

**[06.2 - Bing Search Research Pipeline](06.2-magentic_bing_search_orchestration_tutorial.ipynb)**
Intelligent web research orchestration with fact-checking and comprehensive report generation.

## Prerequisites

### Azure Resources
- Azure AI Project with deployed language model (GPT-4 recommended)
- Azure AI Foundry Project (for Bing Search tutorial)
- Bing Search Connection configured in Azure AI Studio (for tutorial 06.2)

### Environment Variables
Configure your environment in the `.env` file at the project root:

```properties
# Azure AI Configuration (Required for both tutorials)
PROJECT_ENDPOINT="https://your-foundry-resource.services.ai.azure.com/api/projects/your-project-name"
MODEL_DEPLOYMENT_NAME="gpt-4o"  # or your deployed model

# Additional for tutorial 06.2 (Bing Search Research)
AZURE_FOUNDRY_PROJECT_ENDPOINT="https://your-foundry-resource.services.ai.azure.com/api/projects/your-project-name"
```

### Bing Search Setup (for Tutorial 06.2)
Follow the [Bing Search Connection documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/bing-grounding) to configure the Grounding with Bing Search Connection in Azure AI Studio.

### Required Python Packages
```bash
pip install azure-ai-agents azure-identity semantic-kernel azure-ai-projects python-dotenv
```

## Quick Start

```bash
# Clone the repository
git clone https://github.com/Azure-Samples/azure-ai-agents-playbook.git
cd azure-ai-agents-playbook/06-magentic-one-orchestration

# Set up environment variables in .env file at project root
# Run the creative pipeline tutorial
jupyter notebook 06.1-magentic_creative_writing_tutorial.ipynb

# Run the research pipeline tutorial (after setting up Bing Search)
jupyter notebook 06.2-magentic_bing_search_orchestration_tutorial.ipynb
```

## Tutorial Highlights

### Creative Pipeline (06.1)
- Simple architecture with no external API dependencies
- Local plugins for topic selection and haiku classification
- Feedback loops for content quality adjustment
- File operations for temporary haiku analysis
- Random topic selection from predefined list

### Research Pipeline (06.2)
- Bing Search integration with automatic connection discovery
- Complex query decomposition for multi-step research
- Fact verification through cross-referencing multiple sources
- Comprehensive reporting with structured output
- Real-world use case: "43rd president chief of staff education" research


## Next Steps

After mastering Magentic-One orchestration:
- [07-voice-orchestration](../07-voice-orchestration/) - Voice-enabled agent interactions
- [08-agent-routing](../08-agent-routing/) - Hierarchical agent routing patterns
