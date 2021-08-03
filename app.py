from flask import Flask, render_template, Response
from imutils.video import WebcamVideoStream
from flask_cors import CORS
import imutils
import time
import cv2
import datetime

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


def get_camera_test():

    html_source = '''
        <video id="player" controls autoplay></video>
        <button id="capture">Capture</button>
        <canvas id="snapshot" width=320 height=240></canvas>
        <script>
            var player = document.getElementById('player'); 
            var snapshotCanvas = document.getElementById('snapshot');
            var captureButton = document.getElementById('capture');

            var handleSuccess = function(stream) {
                // Attach the video stream to the video element and autoplay.
                player.srcObject = stream;
            };

            captureButton.addEventListener('click', function() {
                var context = snapshot.getContext('2d');
                // Draw the video frame to the canvas.
                context.drawImage(player, 0, 0, snapshotCanvas.width, snapshotCanvas.height);
            });

            navigator.mediaDevices.getUserMedia({video: true}).then(handleSuccess);
        </script>
    '''
    return html_source

@app.route('/cctv-501')
def index():
    """ Video streaming home page """
    return render_template('cctv-501.html')

def stream():
    vs = WebcamVideoStream(src=0).start()
    time.sleep(2.0)
    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=500)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        timestamp = datetime.datetime.now()
        cv2.putText(frame, timestamp.strftime("%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

        cv2.imwrite('cctv.jpg',frame)

        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + open('cctv.jpg', 'rb').read() + b'\r\n')



@app.route('/video_feed')
def video_feed():
    return Response(stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/camera',methods=['GET'])
def get_camera():
    return get_camera_test()

if __name__ == '__main__':
    app.run(host='192.168.0.45', debug=True, port=5000)
