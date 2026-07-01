import os
import shutil
from PIL import Image
import imagehash
from tqdm import tqdm

# =========================
# ตั้งค่า
# =========================

SOURCE_DIR = r"D:\yolo11_project2\img\len"
OUTPUT_DIR = r"D:\yolo11_project2\img\filtered_dataset"

# ยิ่งน้อยยิ่งเข้มงวด
# 0 = เหมือนเป๊ะ
# 5 = คล้ายมาก
# 10 = คล้ายพอสมควร
HASH_THRESHOLD = 8

# =========================
# สร้างโฟลเดอร์ผลลัพธ์
# =========================

output_images = os.path.join(OUTPUT_DIR, "images")
os.makedirs(output_images, exist_ok=True)

# =========================
# ค้นหารูปทั้งหมด
# =========================

image_files = []

for root, dirs, files in os.walk(SOURCE_DIR):

    for file in files:

        if file.lower().endswith(
            (".jpg", ".jpeg", ".png", ".bmp")
        ):
            image_files.append(
                os.path.join(root, file)
            )

print(f"พบรูปทั้งหมด {len(image_files)} รูป")

# =========================
# คัดรูปซ้ำ
# =========================

saved_hashes = []

saved_count = 0
removed_count = 0

for img_path in tqdm(image_files):

    try:

        img = Image.open(img_path)

        # pHash
        current_hash = imagehash.phash(img)

        is_duplicate = False

        for old_hash in saved_hashes:

            distance = current_hash - old_hash

            if distance <= HASH_THRESHOLD:
                is_duplicate = True
                break

        if not is_duplicate:

            dst_name = f"img_{saved_count:06d}.jpg"

            shutil.copy2(
                img_path,
                os.path.join(output_images, dst_name)
            )

            saved_hashes.append(current_hash)

            saved_count += 1

        else:
            removed_count += 1

    except Exception as e:
        print(f"Error: {img_path}")
        print(e)

print("\n========== RESULT ==========")
print(f"รูปต้นฉบับ : {len(image_files)}")
print(f"เก็บไว้     : {saved_count}")
print(f"ตัดออก      : {removed_count}")
print("============================")