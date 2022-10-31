import time
import datetime
import os
import shutil
from tqdm import tqdm

def fileTime(file):   
    t = time.localtime(os.path.getmtime(file))
    return time.strftime("%Y-%m-%d",t)

files_path = "E:/DCIM/100MSDCF/"  # 相机连接到本电脑存储文件路径
Tofiles_path = "相机照片/" #照片需要被存储在本电脑文件夹路径

files_list = os.listdir(files_path)

for i in tqdm(files_list):
    date_name = fileTime(files_path + i)
    # print(files_name)
    if not os.path.exists(Tofiles_path+date_name):
        os.mkdir(Tofiles_path+date_name)#调用系统命令行来创建文件
    file_old_name = files_path + i
    file_new_name = Tofiles_path + date_name +'/' + i
    print((file_old_name,file_new_name))
    if not os.path.exists(file_new_name):
        shutil.copyfile(file_old_name,file_new_name) 
