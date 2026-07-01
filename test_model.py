import cv2
from ultralytics import YOLO

def main():
    # 1. โหลดโมเดลไฟล์ .pt ที่เราเทรนเสร็จล่าสุด (ฉลาดและรันบนคอมได้ลื่นไหลมาก)
    model = YOLO(r"D:\yolo11_project2\runs\detect\train-2\weights\best.pt")

    # 2. เลือกแหล่งข้อมูลภาพที่จะเอามาทดสอบ (เลือกเปิดใช้ออพชันใดออพชันหนึ่งด้านล่างนี้)
    
    # ออพชัน A: เปิดกล้องเว็บแคมคอมพิวเตอร์ของคุณสดๆ (เลข 0 คือกล้องหลักของโน้ตบุ๊ก)
    #source = 0 
    
    # ออพชัน B: หากต้องการทดสอบกับไฟล์วิดีโอที่มีอยู่ในเครื่อง ให้เอาเครื่องหมาย # ด้านล่างออก แล้วใส่พาธไฟล์
    source = r"D:\yolo11_project2\vdo_ex\len\2023_07_09_225642.MOV"

    # เปิดระบบดึงภาพ
    cap = cv2.VideoCapture(source)
    
    print("--- เริ่มทำการทดสอบโมเดล (กดปุ่ม Q บนคีย์บอร์ดเพื่อปิด) ---")

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("ไม่สามารถดึงภาพจากแหล่งข้อมูลได้ หรือวิดีโอจบแล้ว")
            break

        # [เพิ่มโค้ดตรงนี้] ย่อขนาดภาพให้มีความกว้าง 800 พิกเซล (ส่วนความสูงจะคำนวณออโต้ตามสัดส่วนภาพ)
        target_width = 800
        height, width = frame.shape[:2]
        target_height = int(height * (target_width / width))
        frame = cv2.resize(frame, (target_width, target_height))

        # สั่งประมวลผลตามปกติ (ภาพที่ส่งเข้าโมเดลจะเล็กลง หน้าต่างก็จะเล็กลงตาม)
        results = model.predict(source=frame, conf=0.65, device="0", verbose=False)

        # วาดกรอบสี่เหลี่ยมลงบนภาพที่ย่อแล้ว
        annotated_frame = results[0].plot()

        # เปิดหน้าต่างแสดงผลลัพธ์
        cv2.imshow("YOLOv8 Local Test - RTX 3060", annotated_frame)

        # ตั้งค่าให้กดปุ่ม 'q' บนคีย์บอร์ดเพื่อสั่งปิดโปรแกรมทดสอบ
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # เคลียร์ระบบเมื่อปิดโปรแกรม
    cap.release()
    cv2.destroyAllWindows()
    print("--- สิ้นสุดการทดสอบ ---")

if __name__ == '__main__':
    main()