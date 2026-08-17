# 🎙️ PodAI: Podcast Intelligence Agent

PodAI is an agentic, Retrieval-Augmented Generation (RAG) platform that ingests YouTube podcast URLs, extracts timestamps and transcripts, builds local vector embeddings, and enables real-time interactive Q&A and chapter-level summarization.

---


## 🏗️ System Architecture

```text
=======================================================
                PODCAST AGENT FLOW 
=======================================================

  [ PATH A: NEW YOUTUBE URL ]       [ PATH B: FOLLOW-UP QUESTION ]
              │                                   │
              ▼                                   ▼
      get_podcastData()                   search_podcast()
     (Utube_service.py)                  (Utube_service.py)
              │                                   │
              ▼                                   ▼
         Transcript                       Load vector_db/
   (transcript_service.py)             (vector_creation.py)
              │                                   │
              ▼                                   ▼
     HF MiniLM Embeddings             Retrieve Top 5 Chunks
     (vector_creation.py)                 (FAISS Search)
              │                                   │
              ▼                                   ▼
          vector_db/                       Groq LLM API
        (Local FAISS)                (llama-3.3-70b-versatile)
              │                                   │
              ▼                                   ▼
       Initial Summary                       Final Answer
        (via Groq API)                   (Streamlit UI Display)

```

### Key Components

1. **Frontend (`app.py`):** High-aesthetic custom Streamlit UI built with a custom dark glass theme, dynamic session state, active podcast status monitors, and dedicated chat streams.
2. **Agent Orchestration (`agent.py`):** Configured via LangGraph with conversation checkpoint memory (`InMemorySaver`). The system utilizes structured prompt guardrails ensuring tool invocations trigger exclusively for domain-relevant tasks.
3. **Extraction & Processing (`services/`):**
   * `extract_videoid.py`: Sanitizes and parses standard and short-form YouTube links.
   * `transcript_service.py` / `Utube_service.py`: Fetches time-stamped transcript segments and formats raw second offsets into readable `MM:SS` or `HH:MM:SS` chapter markers.
   * `vector_creation.py`: Splits text into semantic chunks and builds vector indexes using `HuggingFaceEmbeddings` (`sentence-transformers/all-MiniLM-L6-v2`) and local `FAISS`.
4. **LLM Engine:** Powered by Groq's LPU Inference Engine using `llama-3.3-70b-versatile` for low-latency reasoning and summarization.

---

## 📁 Repository Structure

```text
Podcast_Agent/
├── agent.py                 # LangGraph Agent definition, system prompt, tool bindings
├── app.py                   # Streamlit web app UI & session controller
├── requirements.txt         # Production dependencies
├── README.md                # System documentation & evaluation
├── .gitignore               # Ignored local files (.venv, .env, __pycache__)
└── services/
    ├── __init__.py          # Service module initialization
    ├── extract_videoid.py   # YouTube URL parsing helper
    ├── transcript_service.py# Transcript fetching & timing conversion
    ├── Utube_service.py     # Agent tool definitions (get_podcastData, search_podcast)
    └── vector_creation.py   # Embedding generation & FAISS vector DB management

```

---------------------------------------------------------------------------------------------

## 🧪 Test & Evaluation Report

| Test ID | Test Scenario | Input Data | Expected Behavior | Actual Behavior | Result |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-01** | **Chit-Chat Guardrail** | `"hi" / "hello"` | Agent responds politely; no tool calls or database searches. | Responded naturally without triggering `get_podcastData` or `search_podcast`. | ✅ **PASS** |
| **TC-02** | **URL Ingestion & Indexing** | Valid YouTube Link | Tool `get_podcastData` called, transcript parsed, vector index created. | FAISS vector store created; generated chapter summary. | ✅ **PASS** |
| **TC-03** | **Timestamp Formatting** | Transcript Extraction | Timestamps formatted in standard `MM:SS` or `HH:MM:SS` (never raw seconds). | Timestamps rendered cleanly as `(02:43 - 03:29)` without floating-point seconds. | ✅ **PASS** |
| **TC-04** | **Targeted Context Retrieval** | `"What was discussed about AI?"` | Tool `search_podcast` retrieves relevant transcript segments; LLM answers strictly on context. | Accurate summary returned with referenced timestamps. | ✅ **PASS** |

### Evaluation Observations
* **Inference Speed:** Transitioning to `llama-3.3-70b-versatile` on Groq dropped token generation latency significantly under 1 second per turn.
* **Embeddings Footprint:** Running `all-MiniLM-L6-v2` locally via HuggingFace provides zero-cost embeddings with minimal memory footprint during vector DB construction.


-------------------------------------------------------------------------------------------------


## 🚀 Installation & Local Setup

Follow these exact steps to run the application locally on Linux, macOS, or Windows:

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/Podcast_Agent.git](https://github.com/YOUR_USERNAME/Podcast_Agent.git)

cd Podcast_Agent

# Create virtual environment
python3 -m venv .venv

# Activate (Linux / macOS)
source .venv/bin/activate

# Activate (Windows PowerShell)
# .venv\Scripts\Activate.ps1


#install dependencies

pip install --upgrade pip
pip install -r requirements.txt

#Create a .env file in the root directory:

touch .env

#Add your Groq API Key inside .env:

GROQ_API_KEY=gsk_your_groq_api_key_here

#Run the app

streamlit run app.py