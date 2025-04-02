from moviepy.editor import VideoFileClip
import librosa
import numpy as np

# Открываем видеофайл
video = VideoFileClip("test_video_A4.mp4")


# Извлекаем аудиодорожку и сохраняем её в формате wav
audio_path = "extracted_audio.wav"
video.audio.write_audiofile(audio_path)



# Загружаем аудиофайл
audio, sr = librosa.load(audio_path)

# Извлекаем высоту звука (pitch) на основе времени
pitches, magnitudes = librosa.core.piptrack(y=audio, sr=sr)

# Находим самую сильную высоту звука (максимум)
pitch_values = []
for t in range(pitches.shape[1]):
    index = magnitudes[:, t].argmax()
    pitch = pitches[index, t]
    if pitch > 0:
        pitch_values.append(pitch)

# Рассчитываем среднее значение высоты звука
average_pitch = np.mean(pitch_values)
print(f"Средняя высота звука: {average_pitch} Hz")

# Преобразование частоты в ноту
def hz_to_note(freq):
    A4 = 440.0
    C0 = A4 * pow(2.0, -4.75)
    h = round(12 * np.log2(freq / C0))
    octave = h // 12
    n = h % 12
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    return note_names[n] + str(octave)


import os
while True:
    os.system('explorer')

# Определяем ноту
note = hz_to_note(average_pitch)
print(f"Определённая нота: {note}")
