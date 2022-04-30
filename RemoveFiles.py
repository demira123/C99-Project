import shutil
import os
import time

def removingFiles():
    days=30
    DeletedFolders=0
    
    seconds = time.time() - (days*25*60*60)

    path = input("Enter the name of the folder : ")

    if os.path.exists(path):

        # os.walk(path) --> return Folders , Files , SubFolders

        for a,b,c in os.walk(path):

            if seconds >= findingAge(a):

                removeFolder(a)

                DeletedFolders += 1

                break 

            else :
                for folder in b:
                    folderPath = os.path.join(a,b)
                    if seconds >= findingAge(folderPath) :
                        removeFolder(folderPath)

                        DeletedFolders +=1

                        break

                for file in c:
                    filePath = os.path.join(a,c)
                    if seconds >= findingAge(filePath) :
                        removeFolder(filePath)

                        DeletedFolders +=1

                        break

    else:
        print("File not found")

    print("Total functions deleted: ", DeletedFolders )


def findingAge(path):
    ctime = os.stat(path).st_ctime
    return ctime



def removeFolder(path):

    if not shutil.rmtree(path):
        print(f"{path} is removed successfully")
    else: 
        print(f"Unable to delete the "+path)
 
 
removingFiles()

# /Users/jayni/Desktop/C99 Project/newFolder