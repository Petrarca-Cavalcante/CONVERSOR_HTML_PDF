from cx_Freeze import setup, Executable
import os

# Additional files to include
include_files = ["path_to_image.png", "data_folder/"]

setup(
    name="Conversor HTML-PDF",
    version="1.0",
    executables=[Executable("starter.pyw", base="Win32GUI")]
)
