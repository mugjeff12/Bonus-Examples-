import zipfile
import pathlib

def make_archive(filepaths,dest_dir):
    destination = pathlib.Path(dest_dir,"Compressed Zip.zip")
    with zipfile.ZipFile(destination,'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)

            archive.write(filepath,arcname=filepath.name)

if __name__ =="__main__":
    make_archive(["Text/a.txt","Text/b.txt","Text/c.txt"],dest_dir='Zip')