import os

def get_all_files(root_folder, files=[]):
    folder_content = os.listdir(root_folder)

    # get all files and folders in folder_content
    subfolders = []
    for i in folder_content:
        full_path = os.path.join(root_folder, i)
        if os.path.isfile(full_path):
            files.append(full_path)
        else:
            subfolders.append(full_path)

    # start recursion on subfolders
    for folder in subfolders:
        get_all_files(folder, files)

    return files

root_folder = r"D:\Work\_PythonSuli\kezdo-230304\my_test_folder"
result = get_all_files(root_folder)
for i in result:
    print(i)