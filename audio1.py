import librosa
import numpy as np

def detect_speech(audio_path, threshold = 0.02):
    data,sample_rate = librosa.load(audio_path, sr = 16000)
    print(type(data))
    frame_length = 1024
    hop_length = 512
    print(data)
    energy = np.array([
        sum(abs(data[i:i+frame_length]**2))
        for i in range(0, len(data), hop_length)
    ])
    print(energy)
    energy = energy / np.max(energy)
    print(energy)
    speech_frames = energy > threshold
    count=0
    for i in range(0, len(data), hop_length):
        if speech_frames[count]:
            yield data[i:i+frame_length]
        count+=1
        


data = []
path = "6.wav"
speech_frames = detect_speech(path)
for i in speech_frames:
    data.extend(i)
print(data)
data = data / np.max(np.abs(data))

import soundfile as sf
output_path = 'output_audio_file.wav'
sf.write(output_path, data, 16000)
