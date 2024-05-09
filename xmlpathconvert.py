import xml.etree.ElementTree as ET
import os
def modify_xml_path(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for path_elem in root.iter('path'):
        path_elem.text = os.path.basename(path_elem.text)

    tree.write(xml_file)

folder_path = '/home/nick/mmyolo/data/welddetect/xml'

for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        modify_xml_path(file_path)

