from services.extract_videoid import extract_video_id
from services.vector_creation import load_vectors
from services.transcript_service import fetch_transcript
from services.vector_creation import split_transcript,create_vectors
from langchain.tools import tool
import os

@tool
def get_podcastData(youtube_url: str) -> str:
    """
    Use this tool ONLY when the user provides a YouTube URL. 
    It downloads the podcast transcript, creates the vector database, and returns initial context.
    The input MUST be a valid YouTube URL string.
    """
    video_id = extract_video_id(youtube_url)

    if not video_id:
        return "Invalid Youtube URL provided."

    transcript = fetch_transcript(video_id)

    if not transcript:
        return "Transcript not available for this video."

    chunks = split_transcript(transcript)
    vector_db = create_vectors(chunks)

    
    retriever = vector_db.as_retriever(search_kwargs={"k": 7})
    docs = retriever.invoke("introduction main topics and summary")

    context = "\n\n".join(doc.page_content for doc in docs)
    return f"Podcast successfully processed! Here is the initial context to generate a summary:\n\n{context}"


@tool 
def search_podcast(query: str) -> str:
    """
    Searches the processed podcast transcript for answers.
    Use this tool when the user asks a specific question about the podcast.
    The input MUST be a plain text search query.
    """

    if not os.path.exists("vector_db/index.faiss"):
        return "System Error: No podcast loaded. Tell the user to provide a YouTube URL first."
    
    vector_db = load_vectors()

    retriever = vector_db.as_retriever(search_kwargs={"k": 5})
    docs = retriever.invoke(query)

    if not docs:
        return "No relevant information found in the transcript."

    context = "\n\n".join(doc.page_content for doc in docs)
    return context