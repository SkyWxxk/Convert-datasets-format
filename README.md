# Convert-datasets-format
Some python script for converting image datasets format. 

## coco2yolo.py
convert coco annotation to yolo annotation.

## coco_split.py
This code is from mmlab which can split dataset to train/val/test sets.

$ python coco_split.py --json NEU-DET/annotations/annotations_all.json --out-dir NEU-DET/annotations/ --ratios 0.85 0.15 --shuffle --seed 10

## fix_coco.py
check and update the image size information in the COCO format JSON annotation file. 

## move_img2file.py
read image filenames from a JSON file and copy these images from a source folder to a target folder. This can be useful when you need to allocate images to different folders (e.g., training set and validation set) based on annotation information.

## xml2coco.py
convert xml annotation to coco annotation.

## xmlpathconvert.py
fix the error xml path. 
