import os 
from pydub import AudioSegment
import speech_recognition as sr 
import moviepy.editor as mp
# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from google.cloud import speech_v1p1beta1 as speech
from pytube import YouTube
from pydub import AudioSegment
from pydub.silence import split_on_silence

ffmpeg = "C:\\Users\\Jacks\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\site-packages\\pydub\\utils.pyffmpeg.exeffmpeg"

r = sr.Recognizer()
# yt = YouTube("https://www.youtube.com/watch?v=3qHkcs3kG44").streams.first().download('C:\\Users\\Jacks\\OneDrive\\Desktop\\Sandbox\\Sandbox')
# clip = mp.VideoFileClip(r"""C:\\Users\\Jacks\\OneDrive\\Desktop\\Sandbox\\Sandbox\\Joe Rogan Experience 1309 - Naval Ravikant.mp4""") 
# converted_clip = clip.audio.write_audiofile(r"""joe_rogan.wav""")
one_eighty_seconds = 180 *1000
podcast = sr.AudioFile(r"""C:\\Users\\Jacks\\OneDrive\\Desktop\\Sandbox\\Sandbox\\joe_rogan.wav""")
# podcast = AudioSegment.from_file("joe_rogan.wav", format= "wav")
# podcast = podcast[:one_eighty_seconds]
with podcast as source:
  r.adjust_for_ambient_noise(source)
  audio = r.record(source, duration= 90)
  audio2 = r.record(source, duration= 90)
  try:
      text = r.recognize_google(audio)
      text2 = r.recognize_google(audio2)
      print('Converting audio transcripts into text ...')
      print(text)
      print("\n")
      print(text2)
  except:
    print('Sorry.. run again...')



