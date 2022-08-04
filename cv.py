import gradio as gr
import time
import requests 
import base64
from PIL import Image
from io import BytesIO
import json


def cnnImageProcessing(image):

    image = image.convert('RGB')

    image.save('inputImage.jpg')

    imageString = gr.processing_utils.encode_url_or_file_to_base64('inputImage.jpg')

    #print(imageString)

    sendRequest = requests.post(url='https://hf.space/embed/sriramelango/MosquitoCNN/api/queue/push/', 
    json={"data": [imageString], "fn_index": 0, "action": "predict", "session_hash": "gix7f5i2p75"})

    hashN = sendRequest.json()['hash'] 
    #print(hashN)

    status = "QUEUED"
    
    statusRequest = requests.post(url='https://hf.space/embed/sriramelango/MosquitoCNN/api/queue/status/', 
    json={"hash": hashN})


    while (status != "COMPLETE"):
        statusRequest = requests.post(url='https://hf.space/embed/sriramelango/MosquitoCNN/api/queue/status/', 
        json={"hash": hashN})
        status = statusRequest.json()['status']
        print(status)
        time.sleep(2)

    #Final Image Processing
    finalImage = statusRequest.json()['data']
    finalImage = (list(finalImage.values()))
    finalImage = finalImage[0][0]
    finalImage = finalImage.replace("data:image/png;base64,", "")

    imgdata = base64.b64decode(finalImage)
    filename = 'proccesedImage.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)
    return filename