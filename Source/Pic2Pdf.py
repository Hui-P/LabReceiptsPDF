import os
import tkinter as tk
from PIL import Image
from tkinter import messagebox

def convert_jpg_to_pdf(input_folder, output_folder):
    # 创建输出文件夹
    os.makedirs(output_folder, exist_ok=True)

    # 遍历输入文件夹中的子文件夹
    for subdir_index, subdir in enumerate(sorted(os.listdir(input_folder))):
        subdir_path = os.path.join(input_folder, subdir)

        # 检查子文件夹是否存在并且是文件夹
        if os.path.isdir(subdir_path):
            # 用于存储原有PDF文件的列表
            original_pdfs = []

            # 遍历子文件夹中的文件
            for file_index, file in enumerate(sorted(os.listdir(subdir_path))):
                file_path = os.path.join(subdir_path, file)

                # 检查文件是否是.jpg格式
                if file.endswith(".jpg"):
                    # 设置输出文件名
                    output_file = f"{subdir}-{file_index + 1}.pdf"
                    output_file_path = os.path.join(output_folder, output_file)

                    # 打开图片并保存为PDF
                    image = Image.open(file_path)
                    rgb_image = image.convert("RGB")
                    rgb_image.save(output_file_path, "PDF", resolution=300.0)
                elif file.endswith(".png"):
                    # 设置输出文件名
                    output_file = f"{subdir}-{file_index + 1}.pdf"
                    output_file_path = os.path.join(output_folder, output_file)

                    # 打开图片并保存为PDF
                    image = Image.open(file_path)
                    rgb_image = image.convert("RGB")
                    rgb_image.save(output_file_path, "PDF", resolution=300.0)
                elif file.endswith(".pdf"):
                    # 将原有PDF文件添加到列表中
                    original_pdfs.append(file_path)

            # 重命名原有的PDF文件
            for i, pdf_path in enumerate(original_pdfs):
                file_name = f"{subdir}({i + 1}).pdf"
                output_file_path = os.path.join(output_folder, file_name)
                os.rename(pdf_path, output_file_path)


# 指定输入文件夹和输出文件夹的路径
input_folder = "Receipt"
output_folder = "Output"

# 调用函数进行转换和复制操作
convert_jpg_to_pdf(input_folder, output_folder)

# 完成打印提示
print("Completed！")
# 创建一个tkinter窗口
window = tk.Tk()
window.withdraw()  # 隐藏主窗口
# 显示完成提示框
messagebox.showinfo("提示", "完成！")
# 关闭窗口
window.destroy()