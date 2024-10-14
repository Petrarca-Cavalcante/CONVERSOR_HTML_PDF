import os
from xhtml2pdf import pisa


def html_pdf_convert(path, final_path):
    path = os.path.normpath(path)
    final_path = os.path.normpath(final_path)


    for html in os.listdir(path):
        if html.endswith(".html"):
            pdf_filename = f"{html[:-5]}.pdf"
            pdf_path = os.path.join(final_path, pdf_filename) 
            
            with open(os.path.join(path, html), 'r', encoding="utf-8") as file:
                with open(pdf_path, 'w+b') as pdf_file:  
                    pisa_status = pisa.CreatePDF(src=file, dest=pdf_file)
                    
                    if pisa_status.err:
                        print(f"Error generating PDF for {html}: {pisa_status.err}")
                    else:
                        print(f"Successfully created {pdf_filename}")


# path = os.path.normpath(r"C:\Users\desenvolvimento\Desktop\1. CERTIDOES HTML")
# final_path = os.path.normpath(r"C:\Users\desenvolvimento\Desktop\CERTIDOES PDF")
