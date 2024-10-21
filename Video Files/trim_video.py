import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from trim_videos_time import path_duration

TRIMMED_FOLDER = 'Video Files/Trimmed Files'

def trim_video(video_path, start_time, end_time):
    if not os.path.exists(video_path):
        print(f"The specified video file does not exist: {video_path}")
        return

    os.makedirs(TRIMMED_FOLDER, exist_ok=True)

    try:
        with VideoFileClip(video_path) as video:
            trimmed_video = video.subclip(start_time, end_time)
            base_name = os.path.basename(video_path)
            file_name, file_extension = os.path.splitext(base_name)
            trimmed_video_path = os.path.join(TRIMMED_FOLDER, f"{file_name}_trimmed{file_extension}")

            trimmed_video.write_videofile(trimmed_video_path, codec="libx264")
            print(f"Trimmed video saved as: {trimmed_video_path}")

    except Exception as e:
        print(f"An error occurred while processing {video_path}: {e}")

if __name__ == "__main__":
    for video_path, start_time, end_time in path_duration:
        trim_video(video_path, start_time, end_time)