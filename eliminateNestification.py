import os
import shutil
import PySimpleGUI as sg

sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('选择目录(例如：D:\\data\\images)')],
          [sg.InputText(), sg.FolderBrowse()],
          [sg.Button('执行'), sg.Button('关闭')]]


def process_dir(path):
    # 遍历所有文件和子目录
    for root, dirs, files in os.walk(path):
        # 对于每个文件夹
        for dir_name in dirs:
            # 如果文件夹的名称与父目录的名称相同
            if dir_name == os.path.basename(root):
                # 递归处理该文件夹
                process_dir(os.path.join(root, dir_name))
                # 遍历该文件夹中的所有文件
                for file_name in os.listdir(os.path.join(root, dir_name)):
                    # 获取文件的完整路径
                    file_path = os.path.join(root, dir_name, file_name)
                    # 将文件移动到父目录
                    shutil.move(file_path, root)
                # 删除嵌套的文件夹
                os.rmdir(os.path.join(root, dir_name))


# Create the Window
window = sg.Window('消除重复目录 v0.0.1 by MrZoyo', layout)

while True:
    event, values = window.read()
    if event in (None, '关闭', sg.WIN_CLOSED):  # if user closes window or clicks cancel
        break
    if event == '执行':
        src_dir = values[0]
        process_dir(src_dir)

        sg.popup('消除完成！')

window.close()
