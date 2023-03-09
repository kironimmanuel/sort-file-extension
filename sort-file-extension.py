import os
import shutil

DOWNLOADS_DIR = os.path.expanduser('~/Downloads')
DOCUMENTS_DIR = f"{DOWNLOADS_DIR}/documents"
MEDIA_DIR = f"{DOWNLOADS_DIR}/media"
IMAGES_DIR = f"{DOWNLOADS_DIR}/images"
SETUP_FILES_DIR = f"{DOWNLOADS_DIR}/setup-files"
COMPRESSED_FILES_DIR = f"{DOWNLOADS_DIR}/compressed-files"
FILES_DIR = f"{DOWNLOADS_DIR}/files"
CODE_DIR = f"{DOWNLOADS_DIR}/code"

os.makedirs(DOCUMENTS_DIR, exist_ok=True)
os.makedirs(MEDIA_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(SETUP_FILES_DIR, exist_ok=True)
os.makedirs(COMPRESSED_FILES_DIR, exist_ok=True)
os.makedirs(FILES_DIR, exist_ok=True)
os.makedirs(CODE_DIR, exist_ok=True)

DOCUMENTS = ['.pdf', '.docx', '.doc', '.txt', '.rtf']
MEDIA = ['.mp4', '.mp3']
IMAGES = ['.jpeg','.jpg','.svg','.png','.PNG','.webp','.ai','.jfif','.xd']
COMPRESSED_FILES = ['.zip']
SETUP_FILES = ['.exe', '.msi']
CODE=['.tsx', '.ts', '.jsx', '.js', ".py", ".c", ".cpp", ".java", ".cs", ".php", ".html", ".css", ".js", ".json", ".xml", ".yml", ".yaml", ".md", ".markdown", ".txt", ".sh", ".bat", ".cmd", ".ps1", ".psm1", ".psd1", ".ps1xml", ".psm1xml", ".psc1", ".psc2", ".mof", ".mfl", ".mfl2", ".msh", ".msh1", ".msh2", ".mshxml", ".msh1xml", ".msh2xml", ".scf", ".lnk", ".inf", ".reg", ".rtf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".tar", ".gz", ".zip", ".7z", ".rar", ".tar.gz", ".tar.bz2", ".tar.xz", ".tar.lzma", ".tar.lz", ".tar.lzo", ".tar.zst", ".tar.Z", ".tar.lz4", ".ta"]
FILES = ['.apk']

for filename in os.listdir(DOWNLOADS_DIR):
    file_path = os.path.join(DOWNLOADS_DIR, filename)
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1].lower()

        if file_extension in DOCUMENTS:
            shutil.move(file_path, DOCUMENTS_DIR)

        elif file_extension in MEDIA:
            shutil.move(file_path, MEDIA_DIR)

        elif file_extension in IMAGES:
            shutil.move(file_path, IMAGES_DIR)

        elif file_extension in SETUP_FILES:
            shutil.move(file_path, SETUP_FILES_DIR)

        elif file_extension in COMPRESSED_FILES:
            shutil.move(file_path, COMPRESSED_FILES_DIR)

        elif file_extension in CODE:
            shutil.move(file_path, CODE_DIR)

        elif file_extension in FILES:
            shutil.move(file_path, FILES_DIR)

