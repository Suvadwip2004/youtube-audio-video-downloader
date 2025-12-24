import os
import yt_dlp  


URL  = input("Enter URL of youtube video : ")

OUTPUT_DIR = "video"

os.makedirs(OUTPUT_DIR, exist_ok=True)


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
