import os
import shutil

desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

folders = {
    "txt": "TextFiles",
    "pdf": "PDFFiles",
    "jpg": "ImageFiles",
    "jpeg": "ImageFiles",
    "png": "ImageFiles",
    "gif": "ImageFiles",
    "heic": "ImageFiles",
    "docx": "WordFiles",
    "pptx": "PowerPointFiles",
    "xlsx": "ExcelFiles",
    "py": "PythonFiles",
    "html": "HTMLFiles",
    "css": "CSSFiles",
    "js": "JSFiles",
    "8xp": "8xpFiles",
    "csv": "CSVFiles",
    "dmg": "DMGFiles",
    "zip": "ZIPFiles",
    "mov": "VideoFiles",
    "mp4": "VideoFiles",
    "jar": "jarFiles"
}

for folder in folders.values():
    folder_path = os.path.join(desktop_path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

for file in os.listdir(desktop_path):
    if os.path.isfile(os.path.join(desktop_path, file)):
        file_extension = file.split(".")[-1].lower()
        if file_extension in folders.keys():
            source_path = os.path.join(desktop_path, file)
            destination_path = os.path.join(desktop_path, folders[file_extension], file)
            shutil.move(source_path, destination_path)
