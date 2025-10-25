# 🎥 YouTube MP3 / MP4 Downloader

Here’s a professional and well-structured `README.md` file tailored for YouTube MP3 / MP4 Downloader.

A simple, modern desktop application for downloading YouTube videos as high-quality MP3 audio or MP4 video files. Built with Python, customtkinter, and yt-dlp

---

## ✨ Features

- Simple Interface: A clean, dark-mode GUI that's easy to navigate.
- Multiple Formats: Download videos as either audio-only (.mp3) or video (.mp4).
- Real-time Progress: A responsive progress bar and status label show download percentage and estimated time remaining (ETA).
- Folder Selection: Use the "Browse" button to easily select where your files are saved.
- Error Handling: Clear pop-up messages for invalid URLs, missing folders, or download failures.
- Cross-Platform: Built with Python, it runs on Windows, macOS, and Linux.

---

## 📋 Requirements

**Before you run the application, you'll need a few things:**

- Python 3.7+

- FFmpeg: This is required by yt-dlp for converting files to MP3 and merging video/audio streams.

- Download: ffmpeg.org/download.html

Installation: You must add the ffmpeg.exe (on Windows) or ffmpeg binary to your system's PATH environment variable so the script can find it.

**Python Libraries:**

- customtkinter
- yt-dlp

## 🚀 Installation & Usage

1. **Clone the repository:**

```bash
git clone https://github.com/AliAsgherZoaib/StreamExtract.git
cd StreamExtract
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

**How To Install FFmpeg:**

- Download the correct version for your operating system from the FFmpeg website (https://ffmpeg.org/download.html).

- Extract the files and add the bin folder (which contains ffmpeg) to your system's PATH.

## 🧪 Usage

1. **Run the application:**
```bash
python StreamExtract.py
```
**How to Download The Video/Audio:**

**1.** Paste your YouTube video URL into the text box.

**2.** Click "Browse" to choose a destination folder.

**3.** Select either "Audio (MP3)" or "Video (MP4)".

**4.** Click "⬇️ Start Download" and wait for the process to complete!

## 🛑 Disclaimer

This project is **not affiliated with YouTube**.

## 🙏 Acknowledgements

CustomTkinter for the modern and beautiful UI components.

yt-dlp for the powerful download logic that makes this all possible.

## 🧠 Credits

Developed by [Ali Asghar Darwala](https://github.com/AliAsgherZoaib)
