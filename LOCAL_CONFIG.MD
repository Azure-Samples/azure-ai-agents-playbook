# ⚙️ Local Environment Setup Guide for Workshop

Follow these step-by-step instructions to get your local development environment ready for the workshop! 🚀

---

## ✅ Step 1: Provision Azure Resources ☁️

Let’s set up everything you need in Azure to run your code with **Azure AI Foundry**.

---

### 1️⃣ Create a Resource Group

1. Go to the [Azure Portal](https://portal.azure.com).
2. Search for and select **Resource Groups**.
3. Click **+ Create** and fill out the form:
   - **Subscription**: Your active subscription
   - **Resource Group name**: `workshop-rg` (or a name of your choice)
   - **Region**: Preferably **East US 2**
4. Click **Review + Create** → **Create**.

---

### 2️⃣ Create an Azure AI Foundry Project 🧠

🔗 **Direct link**: [Create Azure AI Foundry Project](https://portal.azure.com/#create/Microsoft.CognitiveServicesAIFoundry)

1. Open the link above, or in the Azure Portal search for **Azure AI Foundry**.
2. Click **+ Create**, then:
   - Choose **East US 2** as the region.  
     ✅ *Required for service and model availability*
   - Select **Project** (*not Hub-based!*)
   - Leave all other fields at their default values.
3. Click **Review + Create** → **Create**.

> ⚠️ **Important:** Do **not** use a **hub-based** Foundry project. This workshop requires a **project-based** setup.

---

### 🔐 Fix Permissions

After the project is deployed:

- Navigate to your Foundry resource.
- You’ll likely see this message:
  > **"Insufficient permissions: Please assign the Azure AI User role to your user principal."**
- Click the **"Fix me"** button. This assigns the **Azure AI User** role to your account so you can deploy and use models.

---

### 🤖 Deploy Models

In your Azure AI Foundry resource:

1. Open the **Models** section.
2. Click **+ Add** or **Deploy**.
3. Deploy the following models (all **Global Standard** tier):
   - `gpt-4.1`
   - `o1`
   - `o3-mini`
4. Wait for all model deployments to finish before continuing.
 
---

# ⚙️ Local Environment Setup Guide for Workshop

Follow these step-by-step instructions to get your local development environment ready for the workshop!  🚀

---

## 💻 Step 2: Install / Update Azure CLI 🔧

The **Azure CLI (`az`)** is a command-line tool to interact with Azure services from your local terminal.

---

## 📦 Step 3: Clone the Repository 🔁

## 🐍 Step 4: Set Up a Virtual Environment & Install Dependencies

## 🛠️ Step 5: Configure Local Environment Variables 📁

