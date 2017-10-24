import pyaudio, speechkit

FORMAT = pyaudio.paInt16  # глубина звука = 16 бит = 2 байта
CHANNELS = 1  # моно
RATE = 16000  # частота дискретизации - кол-во фреймов в секунду
CHUNK = 4000  # кол-во фреймов за один "запрос" к микрофону - тк читаем по кусочкам

def record(seconds):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    result = b''
    for i in range(0, RATE // CHUNK * seconds):
        data = stream.read(CHUNK)
        result += data

    return result

def play(seconds):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    result = b''
    for i in range(0, RATE // CHUNK * seconds):
        data = stream.read(CHUNK)
        result += data

    return result

data = record(5)

try:
    print(speechkit.record_to_text(data))
except:
    print("Я вас не понял")


