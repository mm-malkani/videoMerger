from moviepy.editor import VideoFileClip, concatenate_videoclips

# Path to your video files
video1_path = "D:\Python Test Cases\Extracted Videos\Video2.mp4"
video2_path = "D:\Python Test Cases\Extracted Videos\Video4.mp4"

# Load video clips
clip1 = VideoFileClip(video1_path)
clip2 = VideoFileClip(video2_path)


# Concatenate videos sequentially
final_clip = concatenate_videoclips([clip1, clip2])

# Save the concatenated video
final_clip.write_videofile('D:\Python Test Cases\Merged Videos\Output4.mp4', codec='libx264', audio_codec='aac')
