from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO
import os
from pdf_generation import pdf
from send_email import email

app = Flask(__name__, template_folder='template', static_folder = 'static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/police')
def police():
    return render_template('police.html')

@app.route('/business')
def business():
    return render_template('business.html')

@app.route('/business_model')
def business_model():
    return render_template('business_model.html')

def gen():
    video_capture = cv2.VideoCapture('Gun-Movies/1-short.mp4')
    model = YOLO('roboflow-v8.pt')

    if not video_capture.isOpened():
        print("Error: Unable to open video file.")
        return
    
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    frame_interval = fps // 1  #1 is 1 frame per second
    frame_count = 0


    while True:
        # Read the next frame
        ret, frame = video_capture.read()

        if not ret:
            break

        if frame_count % frame_interval == 0:
            results = model(frame, conf= 0.5)
            for r in results:
                bboxes = r.boxes.xywh

            if len(bboxes) != 0:
                for box in bboxes:
                    x, y, w, h = box
                    x= int(x.item()) -10
                    y= int(y.item()) -5
                    w= int(w.item())
                    h= int(h.item())
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)  # Draw bounding box 

                save_path = os.path.join("temp", f"frame_{frame_count}.jpg")
                cv2.imwrite(save_path, frame)
            
            frame = cv2.imencode('.jpg', frame)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


        frame_count += 1
    video_capture.release()
    print('model processing done..')

    pdf()

    email()

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)