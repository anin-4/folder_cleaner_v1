import os
import shutil

def ifnotexist(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)

if __name__ == "__main__":
    files=os.listdir()
    files.remove('main.py')
    #print(files)
    other=[]
    images=[".jpeg",".jpg",".png"]
    files_=[".pdf",".txt",".docx"]

    ifnotexist('other')
    ifnotexist('images')
    ifnotexist('files')
    here_goes_my_images=[]
    here_goes_my_files=[]
    for f in files:
        if os.path.splitext(f)[1] in images:
            here_goes_my_images.append(f)
    print(here_goes_my_images)
    for f in files:
        if os.path.splitext(f)[1] in files_:
            here_goes_my_files.append(f)
    print(here_goes_my_files)
    trash=[]
    for f in files:
        if (os.path.splitext(f)[1] not in images) and (os.path.splitext(f)[1] not in files_)and os.path.isfile(f):
            trash.append(f)
    print(trash)

    for image in here_goes_my_images:
        shutil.move(image,'images')
    for f in here_goes_my_files:
        shutil.move(f,'files')
    for o in trash:
        shutil.move(o,'other')

