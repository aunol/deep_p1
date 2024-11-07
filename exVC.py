from TTS.utils.synthesizer import Synthesizer

# 사전 훈련된 한국어 모델을 사용해 합성해보기
synthesizer = Synthesizer(
    "tts_models/ko/kaist/vits",
    vocoder_path=None,
    progress_bar=True
)

# 텍스트를 합성하여 파일로 저장
text = "안녕하세요. 이 목소리는 제 목소리를 학습하여 생성된 음성입니다."
wav = synthesizer.tts(text)
synthesizer.save_wav(wav, "output.wav")
