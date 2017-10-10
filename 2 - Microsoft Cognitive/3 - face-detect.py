import requests

url = "https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize"

headers = {
    "Content-Type": "application/octet-stream",
    "Ocp-Apim-Subscription-Key": "4f2ad86f11724c5287d94a2efb2731c6"
}

data = open('faces.jpg', 'rb').read()

result = requests.post(url, headers=headers, data=data)

faces = result.json()


for face in faces:
    print("x: ", face['faceRectangle']['left'])
    print("y: ", face['faceRectangle']['top'])
    print("width: ", face['faceRectangle']['width'])
    print("height: ", face['faceRectangle']['height'])





    print("--- "*10)
