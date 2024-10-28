import os
from moviepy.editor import VideoFileClip
import moviepy.video.fx.all as vfx

def adjust_trimmed_video_size(input_path, output_path):
    # Load the video clip
    video = VideoFileClip(input_path)
    
    video_duration = video.duration
    adjust_duration = video_duration/10

    # Apply the speed change (slowing down)
    video_slowed = video.fx(vfx.speedx, adjust_duration)
    
    # Write the trimmed video to the new file
    video_slowed.write_videofile(output_path, codec='libx264', audio_codec='aac')

    # Close the video objects
    video_slowed.close()

def trim_videos_in_folder(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Loop through all files in the input folder
    count = 0
    for filename in os.listdir(input_folder):
        # Check if the file is an mp4 file
        if filename.endswith(".mp4"):
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, filename)
            
            print(f"Processing: {filename}")
            try:
                adjust_trimmed_video_size(input_file_path, output_file_path)
                print(f"Saved trimmed video: {output_file_path}")
                count += 1
                print('>>>>>',count)
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Example usage
input_folder = r"D:\videos_trim_script\videos_folder"
output_folder = r"D:\videos_trim_script\trimmed_videos"
trim_videos_in_folder(input_folder, output_folder)
