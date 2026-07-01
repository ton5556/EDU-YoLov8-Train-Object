from ultralytics import YOLO

# 1. ดึงไฟล์โมเดลที่ดีที่สุดที่คุณเพิ่งเทรนเสร็จมาโหลดเข้าโปรแกรม
model = YOLO(r"D:/yolo11_project2/runs/detect/train-2/weights/best.pt")

# 2. สั่งแปลงไฟล์เป็นฟอร์แมต ONNX โดยกำหนดค่าสำหรับสถาปัตยกรรม CPU บนบอร์ด Pi
model.export(format="onnx", imgsz=640, half=False)

print("แปลงไฟล์โมเดลเป็น .onnx สำเร็จแล้ว!")