import os
import subprocess
from tqdm import tqdm

def convert_m4a_to_mp3(source_folder):
    # 存储所有 m4a 文件的列表
    m4a_files = []
    
    # 遍历文件夹下的所有文件和子文件夹
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith(".m4a"):
                # 将 m4a 文件的完整路径添加到列表中
                m4a_files.append(os.path.join(root, file))
    
    # 使用 tqdm 创建进度条
    for m4a_file_path in tqdm(m4a_files, desc="Converting m4a files to mp3"):
        # 创建相同名称的 mp3 文件路径
        mp3_file_path = os.path.splitext(m4a_file_path)[0] + ".mp3"
        
        # 使用 FFmpeg 将 m4a 转换为 mp3
        subprocess.run(['ffmpeg', '-i', m4a_file_path, '-codec:a', 'libmp3lame', '-q:a', '0', mp3_file_path])
        
        # 删除原始的 m4a 文件
        os.remove(m4a_file_path)
        print(f"Converted and removed: {m4a_file_path}")

# 指定需要遍历的文件夹路径
source_folder = '在这里修改路径'
convert_m4a_to_mp3(source_folder)
