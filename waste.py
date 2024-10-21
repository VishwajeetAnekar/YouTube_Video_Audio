# import yt_dlp
# import os
# import subprocess

# YOUTUBE_VIDEO_URL = "https://youtu.be/d_laKxHHPYE"  
# START_TIME = 83  
# END_TIME = 165   
# VIDEO_QUALITY = "1080"  

# def download_youtube_video(download_path='.'):
#     try:
#         ydl_opts = {
#             'format': f'bestvideo[height<={VIDEO_QUALITY}][ext=mp4]',  
#             'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  
#             'progress_hooks': [progress_hook],  
#         }

#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             print("Starting download of the full video...")
#             info_dict = ydl.extract_info(YOUTUBE_VIDEO_URL, download=False)
#             video_title = info_dict['title']
#             ydl.download([YOUTUBE_VIDEO_URL])

#         downloaded_video = os.path.join(download_path, f"{video_title}.mp4")
#         trimmed_video = os.path.join(download_path, f"{video_title}_trimmed.mp4")

#         trim_video(downloaded_video, trimmed_video)

#     except Exception as e:
#         print(f"Error downloading video: {e}")

# def trim_video(input_file, output_file):
#     try:
#         command = [
#             'ffmpeg', '-i', input_file, '-ss', str(START_TIME), '-to', str(END_TIME),
#             '-c', 'copy', output_file
#         ]
#         print(f"Trimming video from {START_TIME}s to {END_TIME}s...")
#         subprocess.run(command, check=True)
#         print("Trimming completed. Saved as:", output_file)

#     except Exception as e:
#         print(f"Error trimming video: {e}")

# def progress_hook(d):
#     if d['status'] == 'downloading':
#         percentage = d['_percent_str']
#         print(f"Downloading... {percentage} completed", end='\r')
#     elif d['status'] == 'finished':
#         print("\nDownload completed!")

# if __name__ == '__main__':
#     download_youtube_video()






#Testing code set 2(tried to trim ) 
# import yt_dlp
# import os
# import subprocess
# from youtube_movies_url import movie_url  

# START_TIME = 83  
# END_TIME = 165   
# VIDEO_QUALITY = "1080"  

# def download_youtube_video(youtube_video_url, download_path='.'):
#     try:
#         ydl_opts = {
#             'format': f'bestvideo[height<={VIDEO_QUALITY}][ext=mp4]',  
#             'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  
#             'progress_hooks': [progress_hook],  
#         }

#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             print(f"Starting download of the video: {youtube_video_url}...")
#             info_dict = ydl.extract_info(youtube_video_url, download=False)
#             video_title = info_dict['title']
#             ydl.download([youtube_video_url])

#         downloaded_video = os.path.join(download_path, f"{video_title}.mp4")
#         trimmed_video = os.path.join(download_path, f"{video_title}_trimmed.mp4")

#         trim_video(downloaded_video, trimmed_video)

#     except Exception as e:
#         print(f"Error downloading video {youtube_video_url}: {e}")

# def trim_video(input_file, output_file):
#     try:
#         command = [
#             'ffmpeg', '-i', input_file, '-ss', str(START_TIME), '-to', str(END_TIME),
#             '-c', 'copy', output_file
#         ]
#         print(f"Trimming video from {START_TIME}s to {END_TIME}s...")
#         subprocess.run(command, check=True)
#         print("Trimming completed. Saved as:", output_file)

#     except Exception as e:
#         print(f"Error trimming video: {e}")

# def progress_hook(d):
#     if d['status'] == 'downloading':
#         percentage = d['_percent_str']
#         print(f"Downloading... {percentage} completed", end='\r')
#     elif d['status'] == 'finished':
#         print("\nDownload completed!")

# if __name__ == '__main__':
#     for url in movie_url:  
#         download_youtube_video(url)  


#Attempt to trim the videos 
# VIDEO_PATH = "D:\Songs\Maiyya Yashoda - Video Song ｜ Hum Saath Saath Hain ｜ Kavita Krishnamurthy ｜ Alka Yagnik.mp4"  
# START_TIME = 120  
# END_TIME = 140    

# def trim_video(video_path, start_time, end_time):
#     if not os.path.exists(video_path):
#         print("The specified video file does not exist.")
#         return

#     try:
#         with VideoFileClip(video_path) as video:
#             trimmed_video = video.subclip(start_time, end_time)
#             base_name = os.path.basename(video_path)
#             file_name, file_extension = os.path.splitext(base_name)
#             trimmed_video_path = os.path.join(os.path.dirname(video_path), f"{file_name}_trimmed{file_extension}")

#             trimmed_video.write_videofile(trimmed_video_path, codec="libx264")
#             print(f"Trimmed video saved as: {trimmed_video_path}")

#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     trim_video(VIDEO_PATH, START_TIME, END_TIME)




#download the best quality video download 
# import yt_dlp
# import os
# from youtube_movies_url import movie_url  

# VIDEO_QUALITY = 'bestvideo'  
# DOWNLOAD_FOLDER = 'downloaded_videos'  
# def download_youtube_video(youtube_video_url, download_path=DOWNLOAD_FOLDER):
#     try:
#         os.makedirs(download_path, exist_ok=True)

#         ydl_opts = {
#             'format': VIDEO_QUALITY + '[ext=mp4]',  
#             'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  
#             'progress_hooks': [progress_hook],  
#         }

#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             print(f"Starting download of the video: {youtube_video_url}...")
#             info_dict = ydl.extract_info(youtube_video_url, download=False)
#             video_title = info_dict['title']
#             ydl.download([youtube_video_url])

#             print(f"Downloaded video: {video_title} to {download_path}")

#     except Exception as e:
#         print(f"Error downloading video {youtube_video_url}: {e}")

# def progress_hook(d):
#     if d['status'] == 'downloading':
#         percentage = d['_percent_str']
#         print(f"Downloading... {percentage} completed", end='\r')
#     elif d['status'] == 'finished':
#         print("\nDownload completed!")

# if __name__ == '__main__':
#     for url in movie_url:  
#         download_youtube_video(url)
