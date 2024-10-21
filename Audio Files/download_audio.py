import yt_dlp
import os
from youtuble_url import song_url  

DOWNLOAD_FOLDER = 'Audio Files/downloaded_mp3s' 

def download_youtube_audio(youtube_video_url, download_path=DOWNLOAD_FOLDER):
    try:
        os.makedirs(download_path, exist_ok=True)

        ydl_opts = {
            'format': 'bestaudio[ext=m4a]',  
            'postprocessors': [{  
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',  # Set desired quality (e.g., '192', '256', '320')
            }],
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'progress_hooks': [progress_hook],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Starting download of the audio from: {youtube_video_url}...")
            info_dict = ydl.extract_info(youtube_video_url, download=False)
            audio_title = info_dict['title']
            ydl.download([youtube_video_url])

            print(f"Downloaded audio: {audio_title} to {download_path}")

    except Exception as e:
        print(f"Error downloading audio from {youtube_video_url}: {e}")

def progress_hook(d):
    if d['status'] == 'downloading':
        percentage = d['_percent_str']
        print(f"Downloading... {percentage} completed", end='\r')
    elif d['status'] == 'finished':
        print("\nDownload completed!")

if __name__ == '__main__':
    for url in song_url:  
        download_youtube_audio(url)


