import pathlib
import shutil
from pathlib import Path

downloads_folder_path = Path("/Users/ericm/Downloads")
programs_path = Path("/Users/ericm/Downloads/Programs")
file_type_variation_list = ['.exe', '.ini', '.zip', '.msi', '.iso', '.torrent']
for file in downloads_folder_path.iterdir():
    if file.is_file():
        extension = file.suffix
        if extension not in file_type_variation_list:
            file_type_variation_list.append(extension)
        if extension == '.exe':
            shutil.move(downloads_folder_path, programs_path)

print(file_type_variation_list)