#!vflask/bin/python3.5
from flask import Flask, render_template, Response
from streamObject import StreamObj
import os 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='MJPEG Streamer')

def gencam(streamer):
    while True:
        frame = streamer.getStreamf()
        yield(b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/imgstream')
def imgstream():
    return Response(gencam(StreamObj()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 9000)))