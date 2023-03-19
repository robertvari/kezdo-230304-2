import os, json
from PIL import Image

def main():
    # get a valid folder path from the user
    folder = get_folder()

    # get all image files
    images = get_images(folder)

    # collect data from images
    photo_data = get_photo_data(images)

    # save image data
    save_data(photo_data)

def get_folder() -> str:
    folder_path = r"D:\Work\_PythonSuli\kezdo-230304\photos\IMG_1070.JPG"
    
    # check path validity
    assert os.path.exists(folder_path), f"A útvonal nem létezik: {folder_path}"

    if os.path.isfile(folder_path):
        folder_path = os.path.dirname(folder_path)

    return folder_path

def get_images(folder) -> list:
    alowed_extensions = [".jpg", ".jpeg"]

    files = []
    for file in os.listdir(folder):
        full_file_path = os.path.join(folder, file)

        # get the file extension. unpacking
        path, ext = os.path.splitext(full_file_path)
        if not ext.lower() in alowed_extensions:
            continue
        
        files.append(full_file_path)
    
    return files

def get_photo_data(images) -> dict:
    photo_data_container = {}

    for image_path in images:
        img = Image.open(image_path)
        
        exif_data = img._getexif()
        if not exif_data:
            continue

        photo_data_container[image_path] = {
            "size": img.size,
            "camera": exif_data.get(0x0110),
            "creation_date": exif_data.get(0x9003),
            "iso": exif_data.get(0x8827)
        }

    return photo_data_container

def save_data(photo_data):
    file_path = "photo_data.json"
    with open(file_path, "w") as my_file:
        json.dump(photo_data, my_file)

    print(f"Data saved to: {file_path}")

main()