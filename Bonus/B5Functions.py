import zipfile

def extract_archive(Archivepath,Destination):
    with zipfile.ZipFile(Archivepath,'r') as archive:
        archive.extractall(Destination)

if __name__== "__main__":
    extract_archive(r'D:\Python Projects\Bonus\Bonus\compressed.zip',r'D:\Python Projects\Bonus\Bonus\Zip')