import os
import shutil

downloads_path = os.path.expanduser("~/Downloads")

folder_names = {
    ".png": "png",
    ".jpg": "jpg",
    ".jpeg": "jpg",
    ".gif": "gif",
    ".bmp": "bmp",
    ".tiff": "tiff",
    ".psd": "psd",
    ".ai": "ai",
    ".eps": "eps",
    ".indd": "indd",
    ".svg": "svg",
    ".mp4": "mp4",
    ".mov": "mov",
    ".wmv": "wmv",
    ".avi": "avi",
    ".mpg": "mpg",
    ".flv": "flv",
    ".swf": "swf",
    ".3gp": "3gp",
    ".m4v": "m4v",
    ".webm": "webm",
    "webp": "webp",
    ".wav": "wav",
    }

for filename in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, filename)
    
    if os.path.isfile(file_path) and any(file_path.lower().endswith(ext) for ext in folder_names.keys()):
        
        file_extension = os.path.splitext(filename)[1].lower()
        
        folder_name = folder_names.get(file_extension, "other")
        
        folder_path = os.path.join(downloads_path, folder_name)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        
        new_file_path = os.path.join(folder_path, filename)
        shutil.move(file_path, new_file_path)
        print(f"Moved {filename} to {folder_name}")

