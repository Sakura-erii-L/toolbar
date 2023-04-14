# IDE: PyCharm
# time: 2023/4/12 15:19
# file: : FIG2PDF.py
# author: Sakura
# Description:fig to pdf

import glob

# TODO: 整合进gui界面，要求：识别图片格式（jpg，png等，输入路径即可转换为PDF



# doc = fitz.open()


def pic2pdf(source_folder):
    doc = fitz.open()
    try:
        print(source_folder)
        source_folder = source_folder + "*" if source_folder.endswith("\\") else source_folder + "\\*"
        print(source_folder)
        for img in sorted(glob.glob(source_folder),
                          key=lambda x: int(str(x).split("4233_")[1].split('-gig')[0])):  # 读取图片，确保按文件名排序
            print('img:', img)
            imgdoc = fitz.open(img)  # 打开图片
            pdfbytes = imgdoc.convert_to_pdf()  # 使用图片创建单页的 PDF
            imgpdf = fitz.open("pdf", pdfbytes)
            doc.insert_pdf(imgpdf)  # 将当前页插入文档
        doc.save("target.pdf")  # 保存pdf文件
    except Exception as e:
        print(e)
        print("目录：[ %s ] 转换pdf异常" % source_folder)
    finally:
        doc.close()


if __name__ == '__main__':
    import fitz

    img_path = input('输入地址：')
    pic2pdf(img_path)
