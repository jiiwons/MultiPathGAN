import os
import shutil
from sklearn.model_selection import train_test_split

# 원본 디렉토리
source_dir = "/mnt/storage01/CSH/한림대/four class original 일대일배정 1000장 이상"

# 새로운 데이터 구조 디렉토리
base_dir = "/mnt/storage01/sjiwon/MultiPathGAN/data/wsi"
train_dir = os.path.join(base_dir, "train")
test_dir = os.path.join(base_dir, "test")
input_sample_dir = os.path.join(base_dir, "input_sample_dir")

# 클래스 지정
classes = ["AGC", "Dysplasia", "EGC", "Normal"]

# 디렉토리 생성
for dir_path in [train_dir, test_dir, input_sample_dir]:
    os.makedirs(dir_path, exist_ok=True)
    for class_name in classes:
        os.makedirs(os.path.join(dir_path, class_name), exist_ok=True)

# 파일 이동 및 분류
for class_name in classes:
    class_source_dir = os.path.join(source_dir, class_name)
    if os.path.isdir(class_source_dir):
        images = [f for f in os.listdir(class_source_dir) if f.endswith(('.jpg', '.jpeg', '.png', '.dcm'))]
        
        # train, test split
        train_images, test_images = train_test_split(images, test_size=0.2, random_state=42)
        
        # train 이미지 이동
        for image in train_images:
            src_path = os.path.join(class_source_dir, image)
            dest_path = os.path.join(train_dir, class_name, image)
            shutil.move(src_path, dest_path)
        
        # test 이미지 이동
        for image in test_images:
            src_path = os.path.join(class_source_dir, image)
            dest_path = os.path.join(test_dir, class_name, image)
            shutil.move(src_path, dest_path)
            
        # input_sample_dir에 일부 이미지 복사 (여기서는 10개 복사)
        sample_images = train_images[:10]  # 첫 10개의 이미지를 복사
        for image in sample_images:
            src_path = os.path.join(train_dir, class_name, image)
            dest_path = os.path.join(input_sample_dir, class_name, image)
            shutil.copy(src_path, dest_path)

