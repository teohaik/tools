import os
import sys
from datetime import datetime


# Python script to add timestamp to WAR files of a folder
# Usage for windows console: 
# addTimestamp.py <FOLDER_CONTAINING_WAR_FILES> (Optional)
# if no argument given, the script considers as working directory the script directory.



if len(sys.argv) > 1:
    print(f'len(sys.argv)  =  {len(sys.argv)}')
    sysPath=sys.argv[1] # position 1 the first argument (if exists). position 0 gives the script file fullpath
else:
    sysPath=sys.path[0]

print(f'current work directory  =  {sysPath}')

dateTimeObj = datetime.now()

print(dateTimeObj.year, '/', dateTimeObj.month, '/', dateTimeObj.day)
print(dateTimeObj.hour, ':', dateTimeObj.minute, ':', dateTimeObj.second, '.', dateTimeObj.microsecond)

DELIMITER="_"

timestamp = str(dateTimeObj.day)+DELIMITER+str(dateTimeObj.month)+DELIMITER+str(dateTimeObj.year)+DELIMITER+str(dateTimeObj.hour)+"."+str(dateTimeObj.minute)

print(f'timestamp= {timestamp}')
filesRenamed=0
for file in os.listdir(sysPath):
    filename = os.fsdecode(file)
    if filename.endswith(".war") and not filename.__contains__(DELIMITER): 
        # print(os.path.join(sysPath, filename))
        oldFilePath=os.path.join(sysPath, filename)
        lastIndexOfDot=filename.rindex(".")
        filenameWithoutType=filename[:lastIndexOfDot]
        filenameWithTimestamp=filenameWithoutType+"-"+timestamp+".war"
        print(f'renaming file {filename} as {filenameWithTimestamp}')
        newFullFilePath=os.path.join(sysPath, filenameWithTimestamp)
        os.rename(oldFilePath,newFullFilePath )
        filesRenamed=filesRenamed+1
        continue
    else:
        continue

print()
print(f"Total files renamed: [{filesRenamed}]")

input("File Renaming finished! Press a key to continue...")
