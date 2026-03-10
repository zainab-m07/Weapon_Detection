import cv2
from ultralytics import YOLO
import os

def get_results(model, frame):

    results = model(frame, show= True, conf= 0.5)
    return results

def extract_frames(video_path, frame_rate=1, display_duration=1000):
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    model = YOLO('roboflow-v8.pt')
    
    # Check if the video file was successfully opened
    if not video_capture.isOpened():
        print("Error: Unable to open video file.")
        return
    
    # Get the frame rate of the video
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    
    # Calculate the frame interval to extract frames at the desired rate
    frame_interval = fps // frame_rate
    
    # Initialize frame counter
    frame_count = 0
    
    while True:
        # Read the next frame
        ret, frame = video_capture.read()
        
        # If there are no more frames, break the loop
        if not ret:
            break
        
        # Check if it's time to display the frame based on the frame rate
        if frame_count % frame_interval == 0:
            # Display the frame
            
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


            cv2.imshow("Frame with Bounding Boxes", frame)
            # Wait for a short time (in milliseconds)
            key = cv2.waitKey(display_duration)

            # If the 'q' key is pressed, break the loop
            if key & 0xFF == ord('q'):
                break
        
        # Increment frame counter
        frame_count += 1
    
    # Release the video capture object
    video_capture.release()
    
    # Close all OpenCV windows
    cv2.destroyAllWindows()

# Example usage

video_path = "Gun-Movies/1-short.mp4"
extract_frames(video_path, frame_rate=1, display_duration=1000)  # Display each frame for 1000 milliseconds (1 second)


