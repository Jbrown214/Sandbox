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
text_storage = []
podcast_text = {}
# idx = 0
with podcast as source:
  # r.adjust_for_ambient_noise(source)
  # r.dynamic_energy_threshold = True
  # r.energy_threshold = 400
  for x in range(0,total_len):
    r.adjust_for_ambient_noise(source)
    r.dynamic_energy_threshold = True
    audio = r.record(source, duration=60)
    podcast_storage["audio{0}".format(x)] = audio

  # text2 = r.recognize_google(podcast_storage['audio129'])#testing line
  # print(text2)
  for keys, values in podcast_storage.items():
    try: 
      text = (r.recognize_google(podcast_storage[keys]))
      # print([x for x in text])
      # pod_list = list(text)
      text_storage.append(text)
      podcast_storage[keys] = text   
    except sr.UnknownValueError:
      continue
    # 
    # print(text_storage[5])
    print(len(text_storage))
    
# print(podcast_storage['audio30'])
# y = json.dumps(list(podcast_storage))
# loaded_json = json.loads(y)
# print(loaded_json['audio0'])

  # with open('speech to text file.txt', 'w') as f:
  #   f.write(json.dumps(list(podcast_storage)))

  # # print(podcast_storage["audio88"])
  # #   # text = r.recognize_google(podcast_storage['audio0'])
  # #   text2 = r.recognize_google(podcast_storage['audio129'])
  # # print(text2)
  # #   # text3 = r.recognize_google(podcast_storage['audio129'])
  # #   # text4 = r.recognize_google(podcast_storage['audio130'])
  # #   for keys, values in podcast_storage.items(): 
  # #     text = r.recognize_google(podcast_storage[keys])
      
  #     # text_storage.append(text)
  # #   # podcast_text_json = json.dumps(podcast_storage)
  # #   # print(len(text_storage))
  # except sr.UnknownValueError:
  #   pass

  # with open('speech to text file.txt', 'w') as f:
  #   f.write(json.dumps(podcast_storage))

  #   # print('Audio transcripts ...\n')
  #   # print(text)
  #   # print("\n")
  #   # print(text2)
  #   # print("\n")
  #   # print(text3)
  #   # print("\n")
  #   # print(text4)
  # # except MemoryError:
  #   print('Sorry.. run again...') 

#   try:
# #       text = r.recognize_google(audio)
# #       text2 = r.recognize_google(audio2)
# #       # text3 = r.recognize_google(audio3)
# #       # text4 = r.recognize_google(audio4)
# #       print('Audio transcripts ...\n')
# #       print(text)
# #       print("\n")
# #       print(text2)
# #       print("\n")
# #       # print(text3)
# #       # print("\n")
# #       # print(text4)
# #   except:
# #     print('Sorry.. run again...')



