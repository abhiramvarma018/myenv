from flask import Flask,render_template,Response
import cv2

app=Flask(__name__)
camera=cv2.VideoCapture(0)

def generate_frames():
    while True:
    
        ##read the camera frame
        success,frame=camera.read()
        if not success:
            break
        else:
            detector = cv2.CascadeClassifier('haar-cascade-files/haarcascade_frontalface_default.xml')
            eye_cascade = cv2.CascadeClassifier('haar-cascade-files/haarcascade_eye.xml')
            faces=detector.detectMultiScale(frame,1.1,7)
            gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            for (x, y, w, h) in faces:
                center = (x+w//2,y+h//2)
                axes=(w//2,h//2)
                cv2.ellipse(frame,center,axes,0,0,360,(255,255,255),2)

                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray,1.1,3)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(frame[y:y+h, x:x+w], (ex, ey), (ex+ew, ey+eh), (128, 128, 128), 2)
            

            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()
            yield(b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n' )

@app.route('/')
def video():
    return render_template('video.html')

@app.route('/capture')
def capture():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__=="__main__":
    app.run(debug=True)