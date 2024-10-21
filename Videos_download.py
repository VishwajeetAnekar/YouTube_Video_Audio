import yt_dlp
import os
from youtube_movies_url import movie_url  

VIDEO_QUALITY = "1080"  
DOWNLOAD_FOLDER = 'downloaded_videos'  

def download_youtube_video(youtube_video_url, download_path=DOWNLOAD_FOLDER):
    try:
        os.makedirs(download_path, exist_ok=True)

        ydl_opts = {
            'format': f'bestvideo[height<={VIDEO_QUALITY}][ext=mp4]',  
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  
            'progress_hooks': [progress_hook],  
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Starting download of the video: {youtube_video_url}...")
            info_dict = ydl.extract_info(youtube_video_url, download=False)
            video_title = info_dict['title']
            ydl.download([youtube_video_url])

            print(f"Downloaded video: {video_title} to {download_path}")

    except Exception as e:
        print(f"Error downloading video {youtube_video_url}: {e}")

def progress_hook(d):
    if d['status'] == 'downloading':
        percentage = d['_percent_str']
        print(f"Downloading... {percentage} completed", end='\r')
    elif d['status'] == 'finished':
        print("\nDownload completed!")

if __name__ == '__main__':
    for url in movie_url:  
        download_youtube_video(url)
