import os 
import json
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
total_len = 132
podcast_storage = {}

with podcast as source:
  # r.adjust_for_ambient_noise(source)
  # r.dynamic_energy_threshold = True
  # r.energy_threshold = 400
  for x in range(0,total_len):
    r.adjust_for_ambient_noise(source)
    r.dynamic_energy_threshold = True
    audio = r.record(source, duration=60)
    podcast_storage["audio{0}".format(x)] = audio

for x in range(0,10):
  try: 
    text = r.recognize_google(podcast_storage["audio{0}".format(x)])
    print(text)
  except sr.UnknownValueError:
    print("audio could not be transcribed")
    continue