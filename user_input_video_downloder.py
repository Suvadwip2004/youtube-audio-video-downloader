import yt_dlp
import os

def get_format_choice(choice):
    formats = {
        "1": "bestvideo[height<=360]+bestaudio/best[height<=360]",
        "2": "bestvideo[height<=480]+bestaudio/best[height<=480]",
        "3": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
        "4": "bestvideo+bestaudio/best"
    }
    return formats.get(choice, formats["4"])  # default = best


def download_youtube_video(url, quality_choice, output_path="video"):
    try:
        # Create folder if not exists
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        format_selected = get_format_choice(quality_choice)

        ydl_opts = {
            'format': format_selected,
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'noplaylist': True,
            'merge_output_format': 'mp4',
            'quiet': False,
            'nocheckcertificate': True,
        }

        print(f"\nDownloading in selected quality...\n")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print(f"\n✅ Download completed! Saved in '{output_path}' folder.")

    except Exception as e:
        print(f"❌ Error: {str(e)}")


def main():
    video_url = input("Enter YouTube URL: ")

    print("\nSelect Video Quality:")
    print("1. 360p")
    print("2. 480p")
    print("3. 1080p")
    print("4. Best Quality")

    choice = input("Enter your choice (1-4): ")

    download_youtube_video(video_url, choice)


if __name__ == "__main__":
    main()