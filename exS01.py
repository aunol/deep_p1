import pandas as pd
from gtts import gTTS
from playsound import playsound

# 텍스트를 음성으로 변환하고 파일로 저장
text = "미나야~안녕? 미나야!바~보 미나야~뭐~~~~~~해?"
tts = gTTS(text=text, lang='ko')
tts.save("save/mina2.mp3")

# 파일 재생
playsound("save/mina2.mp3")
