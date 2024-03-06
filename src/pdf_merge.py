import PyPDF2

def merge_pdfs(pdf1_path, pdf2_path, output_path):
    pdf_writer = PyPDF2.PdfWriter()

    with open(pdf1_path, "rb") as pdf1_file:
        pdf1_reader = PyPDF2.PdfReader(pdf1_file)
        with open(pdf2_path, "rb") as pdf2_file:
            pdf2_reader = PyPDF2.PdfReader(pdf2_file)
            
            num_pages1 = len(pdf1_reader.pages)
            num_pages2 = len(pdf2_reader.pages)
            max_pages = max(num_pages1, num_pages2)
            
            for i in range(max_pages):
                if i < num_pages1:
                    page = pdf1_reader.pages[i]
                    pdf_writer.add_page(page)
                
                if i < num_pages2:
                    page = pdf2_reader.pages[num_pages2 - i - 1]
                    pdf_writer.add_page(page)

    with open(output_path, "wb") as output_pdf:
        pdf_writer.write(output_pdf)

if __name__ == "__main__":
    pdf1 = "front.pdf"
    pdf2 = "back.pdf"
    output = "pfad_zum_zusammengefuegten_pdf.pdf"

    merge_pdfs(pdf1, pdf2, output)
