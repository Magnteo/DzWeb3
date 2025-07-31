from pathlib import Path
import shutil
from concurrent.futures import ThreadPoolExecutor

def zbir_file(source_dir):
    all_file = []
    for file in Path(source_dir).rglob("*"):
        if file.is_file():
            all_file.append(file)

    return all_file

def copy_file(file):
        ext = file.suffix
        ext = ext.lstrip('.')
        name =  file.name

        folder = Path(file).parent / ext
        folder.mkdir(parents=True,exist_ok=True)

        append_folder = folder / name
        print(f"Копіюю {file} - {append_folder}")
 

        shutil.move(str(file), str(append_folder))
        
sourse_dir =r"D:\Users\Admin\Desktop\dist"
all_files = zbir_file(sourse_dir)
with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(copy_file,all_files)
