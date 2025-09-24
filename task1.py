import os
import shutil
import zipfile as zip

""" 
    Report:
        This script prompts the user to enter a folder name, and then creates a specific folder structure inside it. 
        the structure includes sub-directories and text files which are populated with content.
        once made, the title of all the files inside the "docs" folder are changed to lowercase
        Five backup archives of the "docs" folder are then created inside the "store" folder.
        the content of the "store" folder and the content of the first archive are then displayed.    
    
            

    Sources:    
            https://www.geeksforgeeks.org/python-os-path-splitext-method/
            https://www.w3schools.com/python/ref_os_rename.asp                      
"""

def createDirs(surfaceFolder):
    """creates a series of directories and files inside of a folder named by the user. (will be deleted if already existing)

    Args:
        surfaceFolder (string): name of folder to be created
    """
    fileNames = ["HUNTING.txt", "GAMES.txt", "WHEEL.txt", "ARROW.txt", "CROSSBAR.txt"]
    counter = 1
    surfaceAbsPath = os.path.abspath(surfaceFolder)
    
    # if surface directory alrady exists, delete it and then remake it
    if os.path.exists(surfaceAbsPath):
        print("Folder already exists, Deleting...\n")
        shutil.rmtree(surfaceAbsPath)
    os.makedirs(surfaceAbsPath)
    
    # change into surface folder and make 2 dirs
    os.chdir(os.path.join(surfaceFolder))
    os.mkdir("store")
    os.mkdir("keeping")

    #change into "keeping", and make 3 dirs    
    os.chdir(os.path.join("keeping"))
    os.mkdir("pics")
    os.mkdir("docs")
    os.mkdir("movie")
    
    # change into "docs", and make 2 more dirs.
    os.chdir(os.path.join("docs"))
    os.mkdir("work")
    os.mkdir("play")
    
    # staying in "docs", make .txt files and populate them with content
    for name in fileNames:
        with open(name, "w") as file:
            file.write(f"Hello! i am file number {counter}, and my name is: {name}")
            # display message
            print(f"File created in {os.getcwd()}. Name: {name}")
        counter+=1
        
    # return to original directory
    os.chdir(originalDir)

def renameLower():
    """renames all files in the "docs" directory to lowercase.
    """   
    
    # find the path to the docs directory, and change into it
    docsPath = os.path.join(originalDir, folderName, "keeping", "docs")
    os.chdir(docsPath)
    
    # iterate through each file in the folder
    for file in os.listdir():
        # skip folders
        if os.path.isfile(file):
            # separate the name and extension
            name, extension = os.path.splitext(file)
            # create the new name in lowercase, but keep extension as ".txt"
            newName = name.lower() + extension
            # rename the file
            os.rename(file, newName)
            print(f"File: {file} has been renamed to: {newName}")

    # return back to original directory
    os.chdir(originalDir)

def archive():
    """creates five backup archives of the "docs" directory in the "store" dir
    """
    
    # find the path to the "docs" folder
    docsPath = os.path.join(originalDir, folderName, "keeping", "docs")
    # find the path to the store folder
    storePath = os.path.join(originalDir, folderName, "store")

    # create 5 backups of "docs"
    for i in range(1, 6):
        zipName = f"docs_backup_{i}.zip"
        zipPath = os.path.join(storePath, zipName)
        
        # create a zipfile
        with zip.ZipFile(zipPath, "w", zip.ZIP_DEFLATED) as backupZip:
            # walk through "docs" folder and extract all folders and files
            for foldername, subfolders, filenames in os.walk(docsPath):
                # for every file in "docs"
                for file in filenames:
                    # create absolute path of that file
                    filePath = os.path.join(foldername, file)
                    # get the relative path inside the zip file
                    relPath = os.path.relpath(filePath, docsPath)
                    backupZip.write(filePath, relPath)
        
        print(f"archive created in: {zipPath}")

def displayStoreContent():
    """Displays the content of the "store" directory and lists the contents of one backup zip.
    """

    # path to the "store" folder
    storePath = os.path.join(originalDir, folderName, "store")
    os.chdir(storePath)

    # displau "store" folder contents
    print("\nFiles in 'store' folder:\n")
    for file in os.listdir():
        print(file)

    # open one zip file and display its content
    firstZip = os.listdir()[0]  # take the first backup zip
    # open first zip in read mode
    with zip.ZipFile(firstZip, "r") as displayArchive:
        print(f"\nContents of {firstZip}:\n")
        archiveContent = displayArchive.namelist()
        for item in archiveContent:
            print(item)

    # return to original directory
    os.chdir(originalDir)



# get the current working directory so that you have a "savepoint" to return to
originalDir = os.getcwd()
folderName = input("Enter the desired name for a folder: ")
print("=" * 40)
# create the surface path to store all the required folders
createDirs(folderName)
print("=" * 40)
# modify all files to lowercase
renameLower()
print("=" * 40)
# create the archives
archive()
print("=" * 40)
# display content
displayStoreContent()
