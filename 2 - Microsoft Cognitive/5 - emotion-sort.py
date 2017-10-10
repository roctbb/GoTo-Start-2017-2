def emotion_value(x):
    return x[1]


emotions = {
    "anger": 1.0570484E-08,
    "contempt": 1.52679547E-09,
    "disgust": 1.60232943E-07,
    "fear": 6.00660363E-12,
    "happiness": 0.9999998,
    "neutral": 9.449728E-09,
    "sadness": 1.23025981E-08,
    "surprise": 9.91396E-10
}
emotions_list = list(emotions.items())

print(emotions_list[0])
print(emotion_value(emotions_list[0]))

sorted_emotions = sorted(emotions_list, key=lambda x: x[1], reverse=True)

print(sorted_emotions)
print(sorted_emotions[0][0])
