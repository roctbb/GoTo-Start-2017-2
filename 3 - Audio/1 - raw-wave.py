import wave, struct

audio_file = wave.open("task.wav")
n = audio_file.getnframes()

print(audio_file.getparams())

data = audio_file.readframes(n)
print(data[:200])

frames = struct.unpack("@{0}h".format(n), data)
print(frames[:200])

loud_frames = []
for frame in frames:
    loud_frames.append(frame * 10)

print(loud_frames[:200])

loud_data = struct.pack("@{0}h".format(n), *loud_frames)
print(loud_data[:200])

loud_audio_file = wave.open("result.wav", "wb")
loud_audio_file.setparams(audio_file.getparams())
loud_audio_file.writeframes(loud_data)
loud_audio_file.close()


