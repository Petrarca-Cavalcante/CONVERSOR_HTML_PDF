import tkinter as tk
from tkinter import filedialog, messagebox
from main import html_pdf_convert


class ConversorApp:
    def __init__(self, master):
        self.master = master
        master.title("Conversor de HTML para PDF")
        master.geometry("350x300")
        # Título
        self.label = tk.Label(master, text="Conversor de HTML para PDF", font=("Arial", 16))
        self.label.pack(pady=10)

        # Seletor de pasta para HTMLs
        self.html_folder_label = tk.Label(master, text="Pasta com os HTMLs:")
        self.html_folder_label.pack(pady=5)
        self.html_folder_entry = tk.Entry(master, width=50)
        self.html_folder_entry.pack(pady=5)
        self.html_folder_button = tk.Button(master, text="Selecionar Pasta", command=self.select_html_folder)
        self.html_folder_button.pack(pady=5)

        # Seletor de pasta para salvar PDFs
        self.pdf_folder_label = tk.Label(master, text="Salvar PDFs em:")
        self.pdf_folder_label.pack(pady=5)
        self.pdf_folder_entry = tk.Entry(master, width=50)
        self.pdf_folder_entry.pack(pady=5)
        self.pdf_folder_button = tk.Button(master, text="Selecionar Pasta", command=self.select_pdf_folder)
        self.pdf_folder_button.pack(pady=5)

        # Botão Confirmar
        self.confirm_button = tk.Button(master, text="Confirmar", command=self.confirm)
        self.confirm_button.pack(pady=20)

    def select_html_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.html_folder_entry.delete(0, tk.END)
            self.html_folder_entry.insert(0, folder_selected)

    def select_pdf_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.pdf_folder_entry.delete(0, tk.END)
            self.pdf_folder_entry.insert(0, folder_selected)

    def confirm(self):
        html_folder = self.html_folder_entry.get()
        pdf_folder = self.pdf_folder_entry.get() or html_folder

        if not html_folder:
            messagebox.showwarning("Atenção", "Por favor, selecione a pasta com os HTMLs.")
        else:
            html_pdf_convert(path=html_folder, final_path=pdf_folder)
            message = "Conversão concluída!"
            messagebox.showinfo("Confirmação", message)
            
        

if __name__ == "__main__":
    root = tk.Tk()
    app = ConversorApp(root)
    root.mainloop()
