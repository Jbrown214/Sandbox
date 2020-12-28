import speech_recognition as sr 
import moviepy.editor as mp
from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=3qHkcs3kG44").streams.first().download('C:\\Users\\Jacks\\OneDrive\\Desktop\\Sandbox\\Sandbox')
clip = mp.VideoFileClip(r"""C:\\Users\\Jacks\\OneDrive\\Desktop\\Sandbox\\Sandbox\\Joe Rogan Experience 1309 - Naval Ravikant.mp4""") 
clip.audio.write_audiofile(r"""converted.wav""")