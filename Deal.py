import os
import re

def remove_comments(content):
    # 删除单行注释 (// 开头的注释)
    content = re.sub(r'//.*?(\n|$)', '', content)
    # 删除多行注释 (/* */)
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    return content

def process_file(file_path):
    # 打开并读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 删除所有注释
    new_content = remove_comments(content)
    
    # 如果文件内容有变化，写回文件
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f'Processed: {file_path}')
    else:
        print(f'No changes in: {file_path}')

def process_directory(directory):
    # 遍历目录及其子目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.c'):  # 只处理 .c 文件
                file_path = os.path.join(root, file)
                process_file(file_path)

if __name__ == '__main__':
    # 用户输入要处理的目录
    directory = input("Enter the directory to process: ")
    process_directory(directory)
    print("Processing complete!")
