from moviepy.audio.io.AudioFileClip import AudioFileClip
import os
from trim_mp3_path import paths 

output_folder = 'Audio Files/Trimmed Songs'
os.makedirs(output_folder, exist_ok=True)

for file_path, start_time, end_time in paths:
    with AudioFileClip(file_path) as audio:
        trimmed_audio = audio.subclip(start_time, end_time)
        
        base_name = os.path.basename(file_path)
        trimmed_file_name = f'trimmed_{base_name}.mp3'
        trimmed_file_path = os.path.join(output_folder, trimmed_file_name)
        
        trimmed_audio.write_audiofile(trimmed_file_path, codec='libmp3lame')

    print(f'Trimmed audio saved as: {trimmed_file_path}')
