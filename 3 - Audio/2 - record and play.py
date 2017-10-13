import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

# пишем
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                input=True, frames_per_buffer=CHUNK)

print("* recording")

data = b""
for i in range(int(RATE / CHUNK * RECORD_SECONDS)):
    data += stream.read(CHUNK)

print("* done recording")
stream.stop_stream()

# играем
output_stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                       output=True)

output_stream.write(data)
output_stream.close()
