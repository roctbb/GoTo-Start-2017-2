import pyaudio, wave, speechkit

FORMAT = pyaudio.paInt16  # глубина звука = 16 бит = 2 байта
CHANNELS = 1  # моно
RATE = 16000  # частота дискретизации - кол-во фреймов в секунду
CHUNK = 4000  # кол-во фреймов за один "запрос" к микрофону - тк читаем по кусочкам
RECORD_SECONDS = 5  # длительность записи

def record():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    result = b''
    for i in range(0, RATE // CHUNK * RECORD_SECONDS):
        data = stream.read(CHUNK)
        result += data

    return result

data = record()

print(speechkit.record_to_text(data))


