import os
from pypdf import PdfWriter
from PyPDF2 import PdfWriter, PdfReader

#dirc = "C:/Users/HP/python/PycharmProjects/pythonProject/pdf_merge/pdf_files"

inputpdf = PdfReader(open("a.pdf", "rb"))

for i in range(len(inputpdf.pages)):
    output = PdfWriter()
    output.add_page(inputpdf.pages[i])
    with open("doc%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)