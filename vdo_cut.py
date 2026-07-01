import cv2
import os

# ==========================
# Path
# ==========================
video_folder = r'D:\yolo11_project2\vdo_ex\len'
output_root = r'D:\yolo11_project2\img\len'

os.makedirs(output_root, exist_ok=True)

# ==========================
# รองรับไฟล์วิดีโอ
# ==========================
video_extensions = ('.mp4', '.avi', '.mov', '.MOV', '.mkv')

video_files = [
    f for f in os.listdir(video_folder)
    if f.endswith(video_extensions)
]

video_files.sort()

print(f"พบวิดีโอทั้งหมด {len(video_files)} ไฟล์")

# ==========================
# ประมวลผลทีละไฟล์
# ==========================
for idx, video_file in enumerate(video_files, start=1):

    old_video_path = os.path.join(video_folder, video_file)

    # นามสกุลไฟล์เดิม
    ext = os.path.splitext(video_file)[1]

    # ชื่อใหม่
    base_name = f"vdo{idx:03d}"
    new_video_name = f"{base_name}{ext}"
    new_video_path = os.path.join(video_folder, new_video_name)

    # เปลี่ยนชื่อไฟล์วิดีโอ
    if video_file != new_video_name:

        # ถ้ามีชื่อซ้ำอยู่แล้วให้ข้าม
        if not os.path.exists(new_video_path):
            os.rename(old_video_path, new_video_path)
            print(f"{video_file} -> {new_video_name}")
        else:
            print(f"ข้าม {video_file} (มี {new_video_name} อยู่แล้ว)")
            continue

    video_path = new_video_path

    # ==========================
    # สร้างโฟลเดอร์เก็บรูป
    # ==========================
    output_dir = os.path.join(output_root, base_name)
    os.makedirs(output_dir, exist_ok=True)

    print(f"\nกำลังประมวลผล: {new_video_name}")

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("ไม่สามารถเปิดวิดีโอได้")
        continue

    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 30

    print(f"FPS = {fps:.2f}")

    # ==========================
    # เซฟทุก 2 วินาที
    # ==========================
    save_every_frames = int(fps * 2)

    frame_count = 0
    saved_count = 0

    while True:

        success, frame = cap.read()

        if not success:
            break

        if frame_count % save_every_frames == 0:

            # ถ้าต้องการย่อภาพก่อนบันทึก
            # frame = cv2.resize(frame, (1280, 720))

            img_name = os.path.join(
                output_dir,
                f"{base_name}_{saved_count:06d}.jpg"
            )

            cv2.imwrite(img_name, frame)

            saved_count += 1

        frame_count += 1

    cap.release()

    print(f"บันทึกรูป {saved_count} รูป")

print("\nเสร็จสิ้นทั้งหมด")