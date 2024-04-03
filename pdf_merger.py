import os
from pypdf import PdfWriter

#Base project with directory hardcoded.
dirc = "C:/Users/HP/python/PycharmProjects/pythonProject/pdf_merge/pdf_files"

merger = PdfWriter()

#Loop through files within the directory
for file in os.listdir(dirc):
    if not file.endswith(".pdf"):
        continue
    merger.append(file)

#Merge the final file and write in the project directory
merger.write("final_merged.pdf")
merger.close()