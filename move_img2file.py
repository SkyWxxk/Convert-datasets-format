import json
import os
import shutil

#从json读取图片，将图片复制到指定文件夹中
def copy_img(json_file_path,source_folder,target_folder):
    # 确保目标文件夹存在
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # 读取JSON文件
    with open(json_file_path, 'r') as f:
        coco_data = json.load(f)

    # 提取图片文件名
    image_filenames = [image['file_name'] for image in coco_data['images']]

    # 复制图片
    for filename in image_filenames:
        source_path = os.path.join(source_folder, filename)
        target_path = os.path.join(target_folder, filename)
        
        # 如果源文件存在，则复制
        if os.path.exists(source_path):
            shutil.copy2(source_path, target_path)
        else:
            print(f"文件 {filename} 不存在于 {source_folder} 中。")

    print("图片复制完成。")

# JSON文件和文件夹路径
source_folder = '/home/nick/ultralytics/data/NEU-DET/images'

root_path = '/home/nick/ultralytics/data/NEU-DET/'

train_ann = 'annotations/train.json'
val_ann = 'annotations/val.json'
train_img = 'images/train'
val_img = 'images/val'

copy_img(root_path+train_ann,source_folder,root_path+train_img)
copy_img(root_path+val_ann,source_folder,root_path+val_img)