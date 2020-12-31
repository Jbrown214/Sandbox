import os 
from pydub import AudioSegment
import speech_recognition as sr 
import moviepy.editor as mp
# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from pytube import YouTube
from pydub import AudioSegment
import speech_recognition as sr
from pydub.silence import split_on_silence
import speech_recognition as sr 
import os
from pydub import AudioSegment 
from pydub.silence import split_on_silence 
# AudioSegment.converter = r"C:\\Users\\Jacks\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\site-packages\\pydub\\utils.pyffmpeg.exe"
# pydub.AudioSegment.ffmpeg = "C:\\Users\\Jacks\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\site-packages\\pydub\\utils.pyffmpeg.exeffmpeg"
r = sr.Recognizer()
yt = YouTube("https://www.youtube.com/watch?v=3qHkcs3kG44").streams.first().download('C:\\Users\\Jacks\\OneDrive\\Desktop\\Sandbox\\Sandbox')
clip = mp.VideoFileClip(r"""C:\\Users\\Jacks\\OneDrive\\Desktop\\Sandbox\\Sandbox\\Joe Rogan Experience 1309 - Naval Ravikant.mp4""") 
converted_clip = clip.audio.write_audiofile(r"""joe_rogan.wav""")
sixty_seconds = 60 *1000
podcast = sr.AudioFile(r"""C:\\Users\\Jacks\\OneDrive\\Desktop\\Sandbox\\Sandbox\\joe_rogan.wav""")[:sixty_seconds]

with podcast as source:
  r.adjust_for_ambient_noise(source)
  audio = r.record(source, duration =80 )
  try:
      text = r.recognize_google(audio)
      print('Converting audio transcripts into text ...')
      print(text)
  except:
    print('Sorry.. run again...')



