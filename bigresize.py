from PIL import Image
import os

source_folder=r'G:\code\python\SpA-Former-shadow-removal-main\result\epoch_0001'
target_folder=r'G:\code\python\SpA-Former-shadow-removal-main\result\epoch_0001'
file_extension='.png'
new_size=(960,720)
for file_name in os.listdir(source_folder):
    if file_name.endswith(file_extension):
        with Image.open(os.path.join(source_folder,file_name))as img:
            img=img.resize(new_size)
            new_file_name=os.path.splitext(file_name)[0]+file_extension
            img.save(os.path.join(target_folder,new_file_name))