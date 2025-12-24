# YouTube Audio & Video Downloader

A simple Python tool to download audio and video from YouTube. This project provides two separate scripts for downloading YouTube content - one for audio (MP3) and one for video (MP4).

## Features

- 🎵 **Audio Downloader**: Download audio from YouTube videos and convert to MP3 format
- 🎬 **Video Downloader**: Download videos from YouTube in high quality (MP4 format)
- 📁 **Organized Storage**: Automatically saves files to dedicated `audio` and `video` folders
- 🚀 **Easy to Use**: Simple command-line interface

## Requirements

- Python 3.6 or higher
- Required Python packages:
  - `pytubefix` (for audio downloads)
  - `yt-dlp` (for video downloads)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Suvadwip2004/youtube-audio-video-downloader.git
cd FILE
```

2. Install the required dependencies:
```bash
pip install pytubefix yt-dlp
```

Or if you prefer using a requirements file, create one and install:
```bash
pip install -r requirements.txt
```

## Project Structure

```
FILE/
├── youtube_audio_downlode.py    # Audio downloader script
├── youtube_video_downlode.py    # Video downloader script
├── audio/                        # Folder for downloaded audio files
├── video/                        # Folder for downloaded video files
└── README.md                     # This file
```

## Usage

### Download Audio (MP3)

Run the audio downloader script:
```bash
python youtube_audio_downlode.py
```

When prompted, enter the YouTube video URL. The script will:
- Download the audio from the video
- Convert it to MP3 format
- Save it in the `audio` folder

**Example:**
```
YouTube video link : https://www.youtube.com/watch?v=VIDEO_ID
```

### Download Video (MP4)

Run the video downloader script:
```bash
python youtube_video_downlode.py
```

When prompted, enter the YouTube video URL. The script will:
- Download the video in the best available quality
- Save it as MP4 format
- Save it in the `video` folder

**Example:**
```
Enter URL of youtube video : https://www.youtube.com/watch?v=VIDEO_ID
```

## How It Works

### Audio Downloader (`youtube_audio_downlode.py`)
- Uses `pytubefix` library to fetch YouTube video information
- Extracts audio stream from the video
- Downloads the audio file
- Converts the file extension to `.mp3`
- Saves to the `./audio` directory

### Video Downloader (`youtube_video_downlode.py`)
- Uses `yt-dlp` library (a fork of youtube-dl)
- Downloads the best available video and audio streams
- Merges them into a single MP4 file
- Saves to the `video` directory

## Notes

- The `audio` and `video` folders will be created automatically if they don't exist
- Make sure you have a stable internet connection for downloading
- Download times depend on video length and your internet speed
- Some videos may be restricted or unavailable due to regional or copyright restrictions

## Disclaimer

This tool is for educational purposes only. Please respect YouTube's Terms of Service and copyright laws. Only download content that you have permission to download or that is in the public domain.

## License

This project is open source and available for personal use.

## Contributing

Feel free to fork this project and submit pull requests for any improvements!

## Issues

If you encounter any issues:
1. Make sure all dependencies are installed correctly
2. Check that you have a stable internet connection
3. Verify that the YouTube URL is valid and accessible
4. Ensure you have write permissions in the project directory

