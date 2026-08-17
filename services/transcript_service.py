from youtube_transcript_api import YouTubeTranscriptApi
from langchain_core.documents import Document


def fetch_transcript(video_id: str):

    api = YouTubeTranscriptApi()

    try:
        transcript = api.fetch(video_id)

        text = ""

        for snippet in transcript:

            text += (
                f"[{snippet.start:.2f}s] "
                f"{snippet.text} "
            )

        document = Document(
            page_content=text.strip(),
            metadata={
                "video_id": video_id
            }
        )

        return [document]

    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None