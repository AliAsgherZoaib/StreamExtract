import os
import re
import threading
import customtkinter as ctk
from tkinter import filedialog, messagebox
import yt_dlp


#  Validate YouTube URL
def is_valid_youtube_url(url: str) -> bool:
    """Checks if the URL matches a common YouTube video pattern."""
    pattern = r"(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)[\w\-]{11}"
    return bool(re.match(pattern, url))


# Format ETA 
def format_eta(seconds: int | None) -> str:
    """Converts seconds into a MM:SS string."""
    if seconds is None:
        return "N/A"
    try:
        seconds = int(seconds)
        mins, secs = divmod(seconds, 60)
        return f"{mins:02d}:{secs:02d}"
    except (ValueError, TypeError):
        return "N/A"


#Download Function
def download_youtube():
    """
    This function runs in a separate thread.
    It handles the download logic and schedules GUI updates on the main thread.
    """
    url = url_entry.get().strip()
    output_path = folder_path.get()

    default_text_color = title_label.cget("text_color")
    app.after(0, lambda: progress_label.configure(text="", text_color=default_text_color))

    if not url:
        app.after(0, lambda: messagebox.showerror("Error", "Please enter a YouTube URL."))
        app.after(0, lambda: download_btn.configure(state="normal")) # Re-enable button
        return
    if not is_valid_youtube_url(url):
        app.after(0, lambda: messagebox.showerror("Invalid URL", "Please enter a valid YouTube video link."))
        app.after(0, lambda: download_btn.configure(state="normal")) # Re-enable button
        return
    if not output_path:
        app.after(0, lambda: messagebox.showerror("Error", "Please select a download folder."))
        app.after(0, lambda: download_btn.configure(state="normal")) # Re-enable button
        return
    if not is_valid_youtube_url(url):
        app.after(0, lambda: progress_label.configure(text="Error: Please enter a valid YouTube URL.", text_color="#E53935")) # Red
        app.after(0, lambda: download_btn.configure(state="normal")) # Re-enable button
        return
    if not output_path:
        app.after(0, lambda: progress_label.configure(text="Error: Please select a download folder.", text_color="#E53935")) # Red
        app.after(0, lambda: download_btn.configure(state="normal")) # Re-enable button
        return

    download_type = download_option.get()

    # --- Progress Hook (schedules GUI updates) ---
    def progress_hook(d):
        if d['status'] == 'downloading':
            percent_str = d.get('_percent_str', '0.0%').strip()
            eta_str = format_eta(d.get('eta'))
            
            try:
                # Get float value for progress bar
                progress_float = float(percent_str.replace('%', '')) / 100
                
                # Schedule GUI updates on the main thread
                app.after(0, lambda: progress_bar.set(progress_float))
                app.after(0, lambda: progress_label.configure(text=f"Downloading... {percent_str} (ETA: {eta_str})"))
            except ValueError:
                # Handle cases where percent_str might be invalid
                app.after(0, lambda: progress_label.configure(text=f"Downloading... (ETA: {eta_str})"))

        elif d['status'] == 'finished':
            # This just means the file is downloaded, may still be processing (e.g., MP3 conversion)
            app.after(0, lambda: progress_label.configure(text="Download complete. Processing file..."))
            app.after(0, lambda: progress_bar.set(1.0))

    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'progress_hooks': [progress_hook],
        'ignoreerrors': False,
        'noplaylist': True,
        'quiet': True, 
        'no_warnings': False,
        'verbose': True, # Set to True for detailed logs
    }

    if download_type == "mp3":
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        ydl_opts.update({
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'merge_output_format': 'mp4',
        })

    app.after(0, lambda: progress_label.configure(text="Starting download..."))
    app.after(0, lambda: progress_bar.set(0))
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            
            file_name = ydl.prepare_filename(info)
            final_filename = os.path.basename(file_name)
            
            if download_type == "mp3":
                base_name, _ = os.path.splitext(file_name)
                final_file_path = base_name + ".mp3"
                final_filename = os.path.basename(final_file_path)
            else:
                final_file_path = file_name

            if not os.path.exists(final_file_path):
                if os.path.exists(file_name):
                    final_file_path = file_name
                    final_filename = os.path.basename(file_name)
                else:
                    app.after(0, lambda: messagebox.showerror("Error", f"File not found after download:\n{final_file_path}"))
                    app.after(0, lambda: progress_label.configure(text=f"Error: File not found.", text_color="#E53935"))
                    return 

            app.after(0, lambda: progress_label.configure(text=f"✅ Success: Saved {final_filename}", text_color="#43A047")) # Green
            app.after(0, lambda: messagebox.showinfo("Success", f"✅ Downloaded successfully:\n{final_filename}"))

    except Exception as e:
        app.after(0, lambda: progress_label.configure(text=f"Error: Download failed!", text_color="#E53935")) # Red
        app.after(0, lambda: messagebox.showerror("Error", f"Download failed!\n\n{e}"))

    finally:
        app.after(0, lambda: download_btn.configure(state="normal"))


# Threaded Download Starter 
def start_download_thread():
    """
    This function is called by the button.
    It disables the button and starts the download_youtube function in a new thread.
    """
    # Disable button to prevent multiple downloads
    download_btn.configure(state="disabled")
    # Start the download process in a new thread
    threading.Thread(target=download_youtube, daemon=True).start()


#  Choose Folder
def choose_folder():
    """Opens a dialog to select a folder."""
    selected_folder = filedialog.askdirectory()
    if selected_folder:
        folder_path.set(selected_folder)


#  CustomTkinter Setup 
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("🎵 StreamExtract")
# Adjusted window height now that log_box is gone
app.geometry("580x380")
app.resizable(False, False)

# Title 
title_label = ctk.CTkLabel(app, text="🎥 StreamExtract",
                           font=ctk.CTkFont(size=20, weight="bold"))
title_label.pack(pady=10)

#URL
url_label = ctk.CTkLabel(app, text="Enter YouTube URL:")
url_label.pack()
url_entry = ctk.CTkEntry(app, width=460, placeholder_text="Paste YouTube video link here...")
url_entry.pack(pady=8)

# Folder 
folder_frame = ctk.CTkFrame(app)
folder_frame.pack(pady=10)
folder_path = ctk.StringVar()
folder_entry = ctk.CTkEntry(folder_frame, width=340, textvariable=folder_path, placeholder_text="Select download folder...")
folder_entry.pack(side="left", padx=10)
browse_btn = ctk.CTkButton(folder_frame, text="Browse", width=80, command=choose_folder)
browse_btn.pack(side="left")

# Radio Buttons
download_option = ctk.StringVar(value="mp3")
radio_frame = ctk.CTkFrame(app)
radio_frame.pack(pady=5)
ctk.CTkRadioButton(radio_frame, text="Audio (MP3)", variable=download_option, value="mp3").pack(side="left", padx=10)
ctk.CTkRadioButton(radio_frame, text="Video (MP4)", variable=download_option, value="mp4").pack(side="left", padx=10)

# Download Button
download_btn = ctk.CTkButton(app, text="⬇️ Start Download", command=start_download_thread,
                              font=ctk.CTkFont(size=14, weight="bold"))
download_btn.pack(pady=15)

# Progress
progress_bar = ctk.CTkProgressBar(app, width=440)
progress_bar.set(0)
progress_bar.pack(pady=5)

# Progress Label
progress_label = ctk.CTkLabel(app, text="")
progress_label.pack(pady=5)

#  Footer 
footer_label = ctk.CTkLabel(app, text="Files will be saved to your selected folder.",
                           font=ctk.CTkFont(size=12))
footer_label.pack(pady=10)

app.mainloop()
