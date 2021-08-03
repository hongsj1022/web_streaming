class Camera:

    def get_camera_test(self):
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

    def get_file_test(self):
        html_source = '''file
        <input type="file" accept="image/*" capture="camera" id="camera">
        <img id="frame">
        <txt id="txt">
        <script>
            var camera = document.getElementById('camera');
            var frame = document.getElementById('frame');
            var txt = document.getElementById('txt');

            camera.addEventListener('change', function(e) {
                var file = e.target.files[0]; 

                var httpRequest;
                if(window.XMLHttpRequest){
                    httpRequest = new XMLHttpRequest();
                }else if (window.ActiveXObject) {
                    httpRequest = new ActiveXObject("Microsoft.XMLHTTP");
                }
                httpRequest.onreadystatechange = reloadPage
                var reloadPage = function(){
                    txt.write('done')
                }
  
                httpRequest.open('POST', 'http://163.180.117.116:8080/gom/v1/ml/face', true);
                httpRequest.setRequestHeader('Content-Type', 'image/jpeg');
                httpRequest.send(file);

                // Do something with the image file.
                frame.src = URL.createObjectURL(file);
            });
        </script>
        '''
        return html_source

