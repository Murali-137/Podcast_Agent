import streamlit as st
from agent import podcast_agent

st.set_page_config(
    page_title="PodAI | Temporal Intelligence",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- GLOSSY GREEN CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
* { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }

.stApp {
    background-color: #030504;
    background-image: 
        radial-gradient(40vw circle at 15% 20%, rgba(15, 244, 86, 0.08), transparent 100%),
        radial-gradient(40vw circle at 85% 80%, rgba(168, 255, 120, 0.06), transparent 100%),
        radial-gradient(50vw circle at 50% 50%, rgba(230, 249, 157, 0.02), transparent 100%);
    color: #e2e8f0;
    background-attachment: fixed;
}

header { background: transparent !important; }
.block-container { max-width: 1200px; padding-top: 2.5rem; padding-bottom: 6rem; }

[data-testid="stSidebar"] {
    background: rgba(8, 12, 10, 0.70) !important;
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border-right: 1px solid rgba(15, 244, 86, 0.08);
}

.logo {
    font-size: 28px;
    font-weight: 800;
    letter-spacing: -1.5px;
    color: #ffffff;
}

.logo span {
    background: linear-gradient(135deg, #0ff456, #a8ff78);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 20px rgba(15, 244, 86, 0.4);
}

.logo-sub {
    color: #6a8c79;
    font-size: 13px;
    font-weight: 500;
    margin-bottom: 30px;
}

.sidebar-card {
    padding: 14px 16px;
    border-radius: 12px;
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(15, 244, 86, 0.08);
    margin-bottom: 10px;
}

.sidebar-card-title {
    font-size: 13px;
    font-weight: 600;
    color: #e2e8f0;
}

.sidebar-card-sub {
    font-size: 11px;
    color: #6a8c79;
    margin-top: 3px;
}

.hero {
    padding: 10px 0 35px;
    text-align: center;
}

.hero-badge {
    display: inline-flex;
    padding: 6px 14px;
    border-radius: 20px;
    background: rgba(15, 244, 86, 0.08);
    border: 1px solid rgba(15, 244, 86, 0.25);
    color: #0ff456;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 20px;
    box-shadow: 0 0 20px rgba(15, 244, 86, 0.15);
}

.hero h1 {
    font-size: 52px;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.1;
    letter-spacing: -2px;
    margin-bottom: 14px;
}

@keyframes textShine {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.hero h1 span {
    background: linear-gradient(to right, #0ff456, #e6f99d, #0ff456);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: textShine 4s linear infinite;
}

.hero p {
    color: #8da698;
    font-size: 17px;
    max-width: 680px;
    margin: 0 auto;
}

.glass-card {
    background: rgba(10, 15, 12, 0.65);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(15, 244, 86, 0.1);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4), inset 0 0 15px rgba(15, 244, 86, 0.02);
    border-radius: 16px;
    padding: 22px;
    margin-bottom: 20px;
}

.card-title {
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    color: #c0d6c8;
    text-transform: uppercase;
    margin-bottom: 6px;
}

@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(15, 244, 86, 0.4); }
    70% { box-shadow: 0 0 0 6px rgba(15, 244, 86, 0); }
    100% { box-shadow: 0 0 0 0 rgba(15, 244, 86, 0); }
}

.status {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    color: #0ff456;
    font-size: 13px;
    font-weight: 600;
    background: rgba(15, 244, 86, 0.08);
    padding: 6px 14px;
    border-radius: 20px;
    border: 1px solid rgba(15, 244, 86, 0.2);
}

.status-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #0ff456;
    animation: pulse 2s infinite;
    box-shadow: 0 0 10px #0ff456;
}

/* Inputs & Actions */
[data-testid="stTextInput"] input {
    background: rgba(255, 255, 255, 0.02) !important;
    border: 1px solid rgba(15, 244, 86, 0.18) !important;
    border-radius: 12px !important;
    height: 52px !important;
    color: white !important;
}

[data-testid="stTextInput"] input:focus {
    border-color: #0ff456 !important;
    box-shadow: 0 0 0 3px rgba(15, 244, 86, 0.2) !important;
}

.stButton > button {
    width: 100%;
    height: 40px;
    border-radius: 12px;
    border: none;
    background: linear-gradient(135deg, #0bb842 0%, #088c32 100%);
    color: white;
    font-weight: 600;
    box-shadow: 0 4px 15px rgba(15, 244, 86, 0.25);
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(15, 244, 86, 0.4);
    background: linear-gradient(135deg, #0ff456 0%, #0bb842 100%);
    color: #030504;
}

/* Chat Log */
.chat-container { display: flex; flex-direction: column; gap: 18px; margin-top: 10px; }
.message-wrapper { display: flex; flex-direction: column; max-width: 85%; }
.user-wrapper { align-self: flex-end; align-items: flex-end; }
.ai-wrapper { align-self: flex-start; align-items: flex-start; }
.message-label { font-size: 11px; font-weight: 700; margin-bottom: 6px; letter-spacing: 1px; }
.user-label { color: #0ff456; }
.ai-label { color: #a8ff78; }

.chat-bubble {
    padding: 16px 20px;
    border-radius: 16px;
    font-size: 15px;
    line-height: 1.6;
    color: #f1f5f9;
}

.user-bubble {
    background: linear-gradient(135deg, rgba(15, 244, 86, 0.12), rgba(15, 244, 86, 0.03));
    border: 1px solid rgba(15, 244, 86, 0.22);
    border-bottom-right-radius: 4px;
}

.ai-bubble {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(168, 255, 120, 0.12);
    border-bottom-left-radius: 4px;
    backdrop-filter: blur(10px);
}

.footer {
    text-align: center;
    color: #567362;
    font-size: 12px;
    margin-top: 50px;
    padding-top: 20px;
    border-top: 1px solid rgba(15, 244, 86, 0.05);
}
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "processed" not in st.session_state:
    st.session_state.processed = False
if "podcast_url" not in st.session_state:
    st.session_state.podcast_url = ""

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("""
    <div class="logo">Pod<span>AI</span></div>
    <div class="logo-sub">Podcast Intelligence Agent</div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="status" style="margin-bottom: 20px;"><div class="status-dot"></div>Engine Active</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-card">
        <div class="sidebar-card-title">⌁ Vector Space</div>
        <div class="sidebar-card-sub">FAISS Local Index</div>
    </div>
    <div class="sidebar-card">
        <div class="sidebar-card-title">✦ Orchestration</div>
        <div class="sidebar-card-sub">LangChain Agent + Memory</div>
    </div>
    """, unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
<div class="hero">
    <div class="hero-badge">AI PODCAST AGENT</div>
    <h1>Turn long podcasts into<br><span>useful knowledge.</span></h1>
    <p>Provide a YouTube URL to extract transcripts, build a vector space, and interact with the podcast agent.</p>
</div>
""", unsafe_allow_html=True)

# --- TOP INPUT BAR FOR EXPLICIT INITIALIZATION ---
col1, col2 = st.columns([4, 1.2], gap="medium", vertical_alignment="bottom")
with col1:
    url_input = st.text_input(
        "Podcast URL",
        placeholder="https://www.youtube.com/watch?v=...",
        label_visibility="collapsed"
    )
with col2:
    process_btn = st.button("Initialize Agent")

# --- INITIALIZATION LOGIC ---
if process_btn:
    if not url_input.strip():
        st.warning("Please enter a valid YouTube URL.")
    else:
        with st.spinner("Agent initializing: Calling get_podcastData & building Vector DB..."):
            try:
                # Ask podcast agent to process url and return a summary
                prompt = f"Give the summary of this podcast in structured chapters with timestamps: {url_input}"
                response = podcast_agent.invoke(
                    {"messages": [{"role": "user", "content": prompt}]},
                    config={"configurable": {"thread_id": "podcast-session"}}
                )

                content = response["messages"][-1].content
                text_response = content[0]["text"] if isinstance(content, list) else content

                st.session_state.podcast_url = url_input
                st.session_state.processed = True
                st.session_state.messages = []
                st.session_state.messages.append({"role": "user", "content": f"Generate structured podcast summary for: {url_input}"})
                st.session_state.messages.append({"role": "assistant", "content": text_response})
                st.success("Podcast vectorized & summary generated!")
                st.rerun()
            except Exception as e:
                st.error(f"Error processing podcast: {str(e)}")

# --- DYNAMIC ACTIVE STATUS CARD (ONLY SHOWN IF PROCESSED) ---
if st.session_state.processed:
    st.markdown("""
    <div class="glass-card">
        <div class="card-title">AGENT ACTIVATED</div>
        <div class="status"><div class="status-dot"></div>Vector DB Loaded & Ready</div>
    </div>
    """, unsafe_allow_html=True)

# --- CONVERSATION DISPLAY ---
if st.session_state.messages:
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(
                f"""
                <div class="message-wrapper user-wrapper">
                    <div class="message-label user-label">YOU</div>
                    <div class="chat-bubble user-bubble">{msg["content"]}</div>
                </div>
                """, unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div class="message-wrapper ai-wrapper">
                    <div class="message-label ai-label">PODAI AGENT</div>
                    <div class="chat-bubble ai-bubble">{msg["content"]}</div>
                </div>
                """, unsafe_allow_html=True
            )
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div style="height:25px"></div>', unsafe_allow_html=True)

# --- CONDITIONAL CHAT INPUT (ONLY SHOWN IF PROCESSED) ---
if st.session_state.processed:
    user_query = st.chat_input("Ask a follow-up question about the podcast...")
    if user_query:
        st.session_state.messages.append({"role": "user", "content": user_query})

        with st.spinner("Thinking..."):
            try:
                response = podcast_agent.invoke(
                    {"messages": [{"role": "user", "content": user_query}]},
                    config={"configurable": {"thread_id": "podcast-session"}}
                )

                content = response["messages"][-1].content
                text_response = content[0]["text"] if isinstance(content, list) else content

                st.session_state.messages.append({"role": "assistant", "content": text_response})
                st.rerun()

            except Exception as e:
                st.error(f"Agent error: {str(e)}")

# --- FOOTER ---
st.markdown('<div class="footer">PodAI &middot; Agentic LangChain RAG &middot; Conversational Buffer Memory</div>', unsafe_allow_html=True)

