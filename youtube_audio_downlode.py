from pytubefix import YouTube
import os

def download_youtube_audio(url, output_path="./audio"):
    try:
        print("Please wait...")
        yt = YouTube(url)
        print(f"Title: {yt.title}")
        print(f"Channel: {yt.author}")

        
        audio_stream = yt.streams.filter(only_audio=True).first()

        print("Downloading...")
        out_file = audio_stream.download(output_path=output_path)

        
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)

        print(f"Done , Please check :  {new_file}")

    except Exception as e:
        print(" Error :", e)
        

if __name__ == "__main__":
    url = input("YouTube video link : ").strip()
    download_youtube_audio(url)
