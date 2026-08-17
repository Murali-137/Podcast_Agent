from langchain.agents import create_agent
from services.Utube_service import get_podcastData,search_podcast
from langchain.messages import SystemMessage , HumanMessage
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv
import os 

load_dotenv()

client = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
)

memory = InMemorySaver()

system_prompt = """
You are PodAI, a helpful podcast intelligence assistant.

You have two tools:
1. get_podcastData
   - Use ONLY when the user message contains a YouTube URL.
   - This tool processes/loads the podcast.
2. search_podcast
   - Use ONLY when the user asks a specific question about the podcast, topics, speakers, timestamps, or summaries.
   - Do NOT use this tool for casual greetings, chit-chat, or general questions (e.g., "hi", "hello", "who are you?").

IMPORTANT GUIDELINES:
- For greetings or casual conversation, respond politely and directly WITHOUT calling any tool.
- If no podcast has been loaded yet and the user asks about podcast content, politely remind them to provide a YouTube URL first.
- When generating timestamps, always format them in standard human-readable format (MM:SS or HH:MM:SS), NEVER in raw seconds.
"""

podcast_agent= create_agent(
    model =client,
    tools=[get_podcastData,search_podcast],
    system_prompt=SystemMessage(content=system_prompt),
    checkpointer=memory
)
