import os
import PyPDF2
import datetime

merger = PyPDF2.PdfMerger()

pdf_directory = r"C:\course\pdf merger"  # where file is located
for file in os.listdir(pdf_directory):
    if file.endswith(".pdf"):
        file_path = os.path.join(pdf_directory, file)
        merger.append(file_path)

current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")  # as the name suggest

output_directory = r"C:\course\pdf merger\combined" # where file has to save
output_file_path = os.path.join(output_directory, f"CombinedPDF_{current_datetime}.pdf")

merger.write(output_file_path)
merger.close()
