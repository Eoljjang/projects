import os
import shutil


# Creates sub-directories inside of the downloads folder.
def createDirectories():
    folders = ["Pictures", "Media", "Documents", "Packages", "Code", "Folders", "Other"]
    user = 'nathanwong'
    downloadPath = "/Users/{}/Downloads".format(user)
    for folder in folders:
        path = '/Users/{}/Downloads/{}'.format(user, folder)
        if not os.path.exists(path): # If the directory doesn't already exist.
            os.makedirs(path)
        
        # Parses through the downloads folder for matching files, and fills that directory.
        parse(folder, downloadPath, path)

def parse(folder, downloads, destination):
    folders = ["Pictures", "Media", "Documents", "Packages", "Code", "Other"]
    if folder == "Pictures":
        parse = [".jpg", ".jpeg", ".png", ".gif", ".raw", ".svg", ".webp"]
    
    elif folder == "Media":
        parse = [".mp3", ".mp4", ".mov", ".MOV"]

    elif folder == "Documents":
        parse = [".txt", ".rtf", ".doc", ".docx", ".pdf", ".ppt", ".pptx", ".xls", ".xlsx"]

    elif folder == "Packages":
        parse = [".zip", ".tar", ".7z", ".rar", ".tgz"]

    elif folder == "Code":
        parse = [".py", ".c", ".cpp", ".js", ".html", ".css", ".java", ".sql"] # Can be extended.
    
    elif folder == "Folders" or folder == "Other":
        parse = []
    
    # 1) Parse through each file in the downloads folder
    for file in os.listdir(downloads):
        # 2) Then, check if it matches any of the corresponding extensions.
        for extension in parse:
            # 3) If so, add it to the appropriate folder (the current one since we're looping)
            if file.endswith(extension):
                file_path = os.path.join(downloads, file)
                shutil.move(file_path, destination)
    
    # 4) Add all remaining folders in their own directory
    if folder == "Folders":
        for item in os.listdir(downloads):
            item_path = os.path.join(downloads, item)
            if os.path.isdir(item_path) and item not in folders:
                shutil.move(item_path, destination)

    # 5) Add all remaining files into their own directory.
    if folder == "Other":
        exception = downloads + "/.DS_Store" # Bug where DS store is kept and won't allow re-movement.
        for item in os.listdir(downloads):
            item_path = os.path.join(downloads, item)
            if os.path.isfile(item_path) and item not in folders and item_path not in exception:
                shutil.move(item_path, destination)

def main():
    createDirectories()

main()