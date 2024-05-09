import json
import os
from PIL import Image
#检查文件标注是否出错
# COCO标注文件路径和图像文件夹路径
coco_annotation_path = '/home/nick/ultralytics/data/welddetect_ns/annotations/instances_test2017.json'
images_dir = '/home/nick/ultralytics/data/welddetect_ns/test2017'
# 输出的新JSON文件路径
output_json_path = '/home/nick/ultralytics/data/welddetect_ns/annotations/updated_instances_test2017.json'

# 加载COCO标注文件
with open(coco_annotation_path, 'r') as f:
    coco_data = json.load(f)

# 检查并更新图像尺寸
for image in coco_data['images']:
    if image['width'] == 0 or image['height'] == 0:
        # 构建图像的完整路径
        image_path = os.path.join(images_dir, image['file_name'])
        try:
            # 使用Pillow读取图像尺寸
            with Image.open(image_path) as img:
                image['width'], image['height'] = img.size
                print(f"Updated {image['file_name']} with size {img.size}")
        except FileNotFoundError:
            print(f"Image {image['file_name']} not found in {images_dir}")

# 保存更新后的COCO标注到新文件
with open(output_json_path, 'w') as f:
    json.dump(coco_data, f)

print(f"Updated annotations saved to {output_json_path}")

