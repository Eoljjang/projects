import os

# Creates sub-directories inside of the downloads folder.
def createDirectories():
    folders = ["Pictures", "Media", "Documents", "Packages", "Code"]
    user = 'nathanwong'
    for i in folders:
        path = '/Users/{}/Downloads/{}'.format(user, i)
        if not os.path.exists(path): # If the directory doesn't already exist.
            os.makedirs(path)


def main():
    createDirectories()

main()