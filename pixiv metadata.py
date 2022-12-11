#Processes at about 1 second per image 
import os
import subprocess
directory = <folder where your images are>
exiftool = <your exiftool directory>
files = []
location = []
old_location = []


# file iteration and rename
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if not filename in ["desktop.ini","exiftool", "pixiv metadata.py"]: #Check if file IS NOT blacklisted
        files.append(filename.split(".")[0])                            #Creates file array where the tags will get separated
        x = filename.split("#")
        for j in range(len(x)-2):
            x.pop(1)                                                    #Removes the unwanted elements
        new_name = x[0]+x[1]
        old_location.append(os.path.join(directory,filename))
        location.append(os.path.join(directory,new_name))               #Rename the file so exif accepts it

x = 0
for i in range(len(files)):                                             #Execute the file renaming
    os.rename(old_location[x], location[x])
    x=x+1


# data separation and insertion
x = 0
for i in range(len(files)):
    array = files[x].split("#")                                         #Extract everything separated with a #
    title=array[1]
    creator=array[2]
    description=array[3]
    subprocess.call(exiftool+" -overwrite_original"+" -xmp:title="+ "\""+title+"\""+" -xmp:creator="+ "\""+creator+"\""+" -xmp:description="+ "\""+description+ "\" "+ location[x], shell=True)
    x=x+1

