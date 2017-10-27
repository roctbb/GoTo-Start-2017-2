import pyaudio, speechkit, wave


def record(seconds):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    result = b''
    for i in range(0, RATE // CHUNK * seconds):
        data = stream.read(CHUNK)
        result += data
    stream.close()

    return result

def play_file(name):
    file = wave.open(name)
    n = file.getnframes()
    data = file.readframes(n)
    play(data, framerate=file.getframerate())

def play(data, framerate=44100):
    p = pyaudio.PyAudio()
    output_stream = p.open(format=pyaudio.paInt16,
                           channels=1,
                           rate=framerate,
                           output=True)
    output_stream.write(data)
    output_stream.close()

def say(text):
    play_file(speechkit.text_to_record(text))