import os
import tkinter as tk
from PyPDF2 import PdfMerger
from tkinter import messagebox

def merge_pdfs(input_folder, output_file):
    # 获取输入文件夹中的所有PDF文件
    file_list = []
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith('.pdf'):
                file_list.append(os.path.join(root, file))

    # 创建PdfMerger对象
    merger = PdfMerger()

    # 逐个将PDF文件添加到合并器中
    for pdf_file in file_list:
        merger.append(pdf_file)

    # 将合并后的PDF文件保存到输出文件
    merger.write(output_file)

    # 关闭合并器
    merger.close()


# 指定输入文件夹和输出文件的路径
input_folder = 'Output'
output_file = 'Merged/file.pdf'

# 调用函数进行合并
merge_pdfs(input_folder, output_file)

# 完成打印提示
print("Completed！")
# 创建一个tkinter窗口
window = tk.Tk()
window.withdraw()  # 隐藏主窗口
# 显示完成提示框
messagebox.showinfo("提示", "完成！")
# 关闭窗口
window.destroy()