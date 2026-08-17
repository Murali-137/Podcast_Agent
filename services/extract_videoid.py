import re

def extract_video_id(url: str):

    match = re.findall(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    
    if match:
        return match[0] # Returns video_id
    return None