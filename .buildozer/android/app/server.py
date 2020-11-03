# -*- coding: utf-8 -*-
# @时间 : 2020/11/3 9:51 下午
# @作者 : 陈祥安
# @文件名 : server.py
# @公众号: Python学习开发
from flask import Flask, request
from werkzeug.utils import secure_filename
from PIL import Image
import time

app = Flask(import_name="FlaskUpload")
cam_width = 0
cam_height = 0


@app.route("/camSize", methods=["post"])
def cam_size():
    global cam_width
    global cam_height
    cam_width = int(float(request.args["width"]))
    cam_height = int(float(request.args["height"]))
    print("width", cam_width, "&Height", cam_height, "Received Successfully.")
    return


@app.route("/index")
def index():
    return "hello"


@app.route('/', methods=['POST'])
def upload_file():
    global cam_width
    global cam_height
    file_to_upload = request.files['media'].read()
    image = Image.frombytes(mode="RGBA", size=(cam_width, cam_height), data=file_to_upload)
    image.save(f'{int(time.time())}.png')
    print('File Uploaded Successfully.')
    return 'SUCCESS'


# http://192.168.199.169:9999/index
app.run(host="0.0.0.0", port=9999, debug=True)
