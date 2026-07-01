from ultralytics import YOLO

def main():
    model = YOLO(r'D:/yolo11_project2/yolov8n.pt')

    train_results = model.train(
        data=r"D:/yolo11_project2/datasets/data.yaml",  # พาธไฟล์ yaml ของคุณ
        epochs=1000,         
        imgsz=640,           
        device="0",           
        workers=2,            # ลองขยับเป็น 2 เพื่อให้ CPU ช่วยส่งภาพให้การ์ดจอไวขึ้น 
        batch=16,             # ส่งภาพเข้าการ์ดจอทีละ 16 รูป (RTX 3060 6GB รับไหวสบายๆ)
        patience=50,          # ถ้าเทรนไป 50 รอบแล้วไม่เก่งขึ้น ให้หยุดเทรนทันที (ป้องกัน Overfitting)
        save=True             # สั่งให้เซฟไฟล์ผลลัพธ์ลงเครื่องถาวร
    )

if __name__ == '__main__':
    main()