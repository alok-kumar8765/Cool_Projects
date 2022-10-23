import moviepy.editor

video = moviepy.editor.videoFileClip("video_name.mp4")
audio = video.audio
audio.write_audiofile('extracted.mp3')
