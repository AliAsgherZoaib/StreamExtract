🎥 YouTube MP3 / MP4 Downloader

A simple, modern desktop application for downloading YouTube videos as high-quality MP3 audio or MP4 video files. Built with Python, customtkinter, and yt-dlp.

✨ Features

Simple Interface: A clean, dark-mode GUI that's easy to navigate.

Multiple Formats: Download videos as either audio-only (.mp3) or video (.mp4).

Real-time Progress: A responsive progress bar and status label show download percentage and estimated time remaining (ETA).

Folder Selection: Use the "Browse" button to easily select where your files are saved.

Error Handling: Clear pop-up messages for invalid URLs, missing folders, or download failures.

Cross-Platform: Built with Python, it runs on Windows, macOS, and Linux.

📋 Requirements

Before you run the application, you'll need a few things:

Python 3.7+

FFmpeg: This is required by yt-dlp for converting files to MP3 and merging video/audio streams.

Download: ffmpeg.org/download.html

Installation: You must add the ffmpeg.exe (on Windows) or ffmpeg binary to your system's PATH environment variable so the script can find it.

Python Libraries:

customtkinter

yt-dlp

🚀 Installation & Usage

Clone the repository:

git clone [https://github.com/AliAsgherZoaib/StreamExtract.git]
cd StreamExtract


Install the required Python packages:

pip install -r requirements.txt

Install FFmpeg:

Download the correct version for your operating system from the FFmpeg website.

Extract the files and add the bin folder (which contains ffmpeg) to your system's PATH.

Run the application:

python StreamExtract.py


How to Download:

Paste your YouTube video URL into the text box.

Click "Browse" to choose a destination folder.

Select either "Audio (MP3)" or "Video (MP4)".

Click "⬇️ Start Download" and wait for the process to complete!

🙏 Acknowledgements

CustomTkinter for the modern and beautiful UI components.

yt-dlp for the powerful download logic that makes this all possible.