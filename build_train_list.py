import os
import glob

# 指定目录
dir_path = "G:\code\python\SpA-Former-shadow-removal-main/my_data/test_A"

# 获取目录中的所有图片文件
img_files =  glob.glob(os.path.join(dir_path, "*.png"))

# 将所有文件名保存到txt中
with open("val_list.txt", "w") as f:
    for img_file in img_files:
        f.write(os.path.basename(img_file) + "\n")
