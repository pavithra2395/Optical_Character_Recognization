import os
from pdf2image import convert_from_path

# Path to the directory containing the PDFs
pdf_dir = 'C:\\Users\\rndbcpsoft\\pdf_extraction\\AHI\\'

# Loop through each PDF file in the directory
for pdf_file in os.listdir(pdf_dir):
    if pdf_file.endswith('.pdf'):
        # Create a folder for the images of this PDF
        pdf_name = pdf_file[:-4]  # Remove the .pdf extension
        image_dir = os.path.join(pdf_dir, pdf_name)
        os.makedirs(image_dir, exist_ok=True)

        # Convert the PDF to images and save them in the folder
        pages = convert_from_path(os.path.join(pdf_dir, pdf_file))
        for i, page in enumerate(pages):
            image_path = os.path.join(image_dir, f'{pdf_name}_page{i + 1}.jpg')
            page.save(image_path, 'JPEG')