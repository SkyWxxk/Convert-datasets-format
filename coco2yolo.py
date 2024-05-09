import json
import os

# COCO标注文件路径
coco_annotation_path = '/home/nick/ultralytics/data/NEU-DET/annotations/val.json'
# YOLO标注文件保存目录
yolo_annotation_dir = '/home/nick/ultralytics/data/NEU-DET/labels/val/'

# 确保YOLO标注目录存在
os.makedirs(yolo_annotation_dir, exist_ok=True)

# 加载COCO标注文件
with open(coco_annotation_path, 'r') as f:
    coco_annotations = json.load(f)

# 构建类别索引映射
category_id_to_index = {category['id']: idx for idx, category in enumerate(coco_annotations['categories'])}

# 处理每个标注
for image_info in coco_annotations['images']:
    image_id = image_info['id']
    file_name = image_info['file_name']
    # 使用图片文件名（不包括扩展名）作为YOLO标注文件的名称
    base_name = os.path.splitext(file_name)[0]
    yolo_annotation_path = os.path.join(yolo_annotation_dir, f"{base_name}.txt")
    
    # 清空或创建标注文件
    with open(yolo_annotation_path, 'w') as f:
        pass

    # 查找与当前图片ID匹配的所有标注
    annotations = [ann for ann in coco_annotations['annotations'] if ann['image_id'] == image_id]
    for annotation in annotations:
        category_id = annotation['category_id']
        bbox = annotation['bbox']
        width, height = image_info['width'], image_info['height']

        # 转换为YOLO格式
        x_center = (bbox[0] + bbox[2] / 2) / width
        y_center = (bbox[1] + bbox[3] / 2) / height
        w = bbox[2] / width
        h = bbox[3] / height

        # 构建YOLO格式的标注字符串
        yolo_format_annotation = f"{category_id_to_index[category_id]} {x_center} {y_center} {w} {h}\n"

        # 追加到YOLO标注文件
        with open(yolo_annotation_path, 'a') as f:
            f.write(yolo_format_annotation)

