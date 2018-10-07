#!/usr/bin/env python
from flask import Flask, jsonify, send_from_directory, request
from services.image_mask import  HSV
import base64
import  cv2
app = Flask(__name__)

hsv_object=None

@app.route('/')
def index():
    return send_from_directory("templates", "index.html")

@app.route('/inputImage', methods=['POST'])
def inputImage():
    content = dict(request.json)
    print(content)
    hsv_object= HSV(content['inputImage'])
    global hsv_object
    return "Uploaded"




@app.route('/sendHSV', methods=['POST'])
def sendHSV():
    content = dict(request.json)
    print(content)
    global hsv_object
    result=hsv_object.select_color(content)
    _, buffer = cv2.imencode('.jpg', result)
    jpg_as_text = base64.b64encode(buffer)


    return jpg_as_text



if __name__ == '__main__':
    app.debug = True
    app.run()
print('Started')