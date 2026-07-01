from ultralytics import YOLO

model = YOLO(r'D:\yolo11_project2\runs\detect\train-2\weights\best.pt')

results = model(r'D:\yolo11_project2\datasets\test\images\vdo2-36-_jpg.rf.775f0243475bd62ef8de77250ccfcbee.jpg',)
results[0].show()