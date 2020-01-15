import moviepy.editor as mp;
from mutagen.mp3 import MP3;
def merge_AudioVideo():
	audio = MP3("music.mp3");
	video = mp.VideoFileClip("current.mp4").subclip(0,audio.info.length);
	video.write_videofile("meme.mp4", audio="music.mp3");

merge_AudioVideo();
