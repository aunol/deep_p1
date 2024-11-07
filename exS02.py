import pandas as pd
from gtts import gTTS
from playsound import playsound

# 구분자 없이 파일을 읽기 위해 한 줄씩 읽기
with open("data/korean/nsmc/ratings_train.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# 첫 번째 줄은 헤더이므로 제외하고 4줄만 선택
texts = [line.strip().split("\t")[1] for line in lines[7:12]]  # 텍스트가 두 번째 열에 있다고 가정

# 텍스트들을 하나로 합치기
combined_text = ' '.join(texts)

# 텍스트를 음성으로 변환
tts = gTTS(text=combined_text, lang='ko')

# 음성 파일로 저장
tts.save("textb/combined_audio1.mp3")

# 파일 재생
playsound("textb/combined_audio1.mp3")
