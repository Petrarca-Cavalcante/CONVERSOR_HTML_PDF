import os 
import win32com.client



def html_pdf_convert(path, final_path):
    path = os.path.normpath(path)
    final_path = os.path.normpath(final_path)


    for html in os.listdir(path):
        if html.endswith(".html"):
            pdf_filename = f"{html[:-5]}.pdf"
            pdf_path = os.path.join(final_path, pdf_filename) 
            html_path = os.path.join(path, html)

            word = win32com.client.Dispatch('Word.Application')
            doc = word.Documents.Open(html_path)
            doc.SaveAs(pdf_path, FileFormat=17)
            doc.Close()
            word.Quit()