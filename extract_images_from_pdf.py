
# pip install fitz PyMuPDF

import fitz
import re
import os

file_path = r'1.pdf' # PDF 文件路径
dir_path = r'imgs' # 存放图片的文件夹

def pdf2image1(path, pic_path):
    checkIM = r"/Subtype(?= */Image)"
    pdf = fitz.open(path)
    lenXREF = pdf.xref_length()
    count = 1
    for i in range(1, lenXREF):
        text = pdf.xref_object(i)
        isImage = re.search(checkIM, text)
        if not isImage:
            continue
        pix = fitz.Pixmap(pdf, i)
        new_name = f"img_{count}.png"
        pix.writePNG(os.path.join(pic_path, new_name))
        count += 1
        pix = None

pdf2image1(file_path, dir_path)

