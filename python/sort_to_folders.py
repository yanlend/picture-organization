from tkinter import Tk
from tkinter.filedialog import askdirectory
import shutil
import os
from PIL import Image


def get_date_taken(path):
    return Image.open(path)._getexif()[36867]


def move_pictures_dated_folder(inpath, outpath):
    image_names = os.listdir(inpath)
    for img_name in image_names:
        print("Processing", img_name)
        img_path = os.path.join(inpath, img_name)
        if os.path.isdir(img_path) or not os.path.splitext(img_path)[1].lower() == ".jpg":
            continue

        img_date = get_date_taken(img_path).split()[0].replace(":", "_")

        out_folders = os.listdir(outpath)
        move_ok = False
        for out_candidate in out_folders:
            if out_candidate.startswith(img_date):
                out_folder = os.path.join(outpath, out_candidate)
                shutil.move(img_path, out_folder)
                move_ok = True
                break
        if not move_ok:
            print("No folder found for date {}, creating new...".format(img_date))
            out_folder = os.path.join(outpath, img_date)
            os.mkdir(out_folder)
            shutil.move(img_path, out_folder)


if __name__ == "__main__":
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    inpath = askdirectory(title="Source path") # show an "Open" dialog box and return the path to the selected file
    if inpath == "":
        raise UserWarning("Must select source path with all pictures")
    outpath = askdirectory(title="Destination path")
    if outpath == "":
        raise UserWarning("Must select destination path with folders")
    print("Copying from ", inpath, "to", outpath)

    move_pictures_dated_folder(inpath, outpath)
    print("Done")

    # inpath = "C:/temp/2018_04_22 Babybauchfoto"
    # outpath = "C:/temp/dest"
    # move_pictures_dated_folder(inpath, outpath)
