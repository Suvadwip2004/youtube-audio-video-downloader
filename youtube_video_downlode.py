import os
import yt_dlp  

# YouTube URL (REPLACED as requested)
URL  = input("Enter URL of youtube video : ")
# URL = ""
# TARGET directory
OUTPUT_DIR = "video"

# Create directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
# Present directory
# OUTPUT_DIR = os.getcwd()

def download_video(url):
    ydl_opts = {
        "outtmpl": os.path.join(OUTPUT_DIR, "%(title)s.%(ext)s"),
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "quiet": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("\n[+] Download completed!")
    print("[+] Saved in:", OUTPUT_DIR)

if __name__ == "__main__":
    download_video(URL)
