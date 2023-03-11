import PyPDF2
import os

# PDF file path
pdf_folder = "Your File Path"
#pdf_folder = os.path.abspath(os.getcwd())
print(pdf_folder)
# Read Pdf Files
for filename in os.listdir(pdf_folder):
    if filename.endswith('.pdf'):
        pdf_file = open(os.path.join(pdf_folder, filename), 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Read specific PDF file
        page = pdf_reader.pages[0]

        # Use only strings (its optinals)
        tc = [word for word in page.extract_text().split()[3:7] if word.isalpha()]

        new_file_name = '_'.join(tc) + '.pdf'
        # Create new named file in another folder
        os.makedirs(pdf_folder + '/Renamed_PDF', exist_ok=True)
        with open(os.path.join(pdf_folder + '/Renamed_PDF', new_file_name), 'wb') as new_file:
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(page)
            pdf_writer.write(new_file)

        pdf_file.close()
