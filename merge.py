from moviepy.editor import VideoFileClip, concatenate_videoclips

# Path to your video files
video1_path = "D:\Python Test Cases\Extracted Videos\Video2.mp4" #Path of video file 1
video2_path = "D:\Python Test Cases\Extracted Videos\Video4.mp4" #Path of video file 2

# Load video clips
clip1 = VideoFileClip(video1_path)
clip2 = VideoFileClip(video2_path)


# Concatenate videos sequentially
final_clip = concatenate_videoclips([clip1, clip2])

# Save the concatenated video
final_clip.write_videofile('' , codec='libx264', audio_codec='aac')
