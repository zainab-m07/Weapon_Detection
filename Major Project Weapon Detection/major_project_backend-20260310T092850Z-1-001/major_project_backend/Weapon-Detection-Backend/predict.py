from ultralytics import YOLO

def get_results():
    model = YOLO('roboflow-v8.pt')
    results = model(source= 'test-image.png', show= True, conf= 0.5)
    
get_results()