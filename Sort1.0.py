import os,shutil
#Tells the program what the path is.
path = r"/Users/conniewunder/Desktop/Testsortingfiles/"

#Tells the program the files' names. 
file_names = os.listdir(path)

#Tells the program what the names are.
sortnames = ['SocialStudies','Science','Math']


#This stuff down here says to create a file named one of the three names in "sortnames" if there isn't already a file called that.
for loop in range(0,3):
    if not os.path.exists(path + sortnames[loop]):
        print(path + sortnames[loop])
        os.makedirs((path + sortnames[loop]))


#This block of code tells the program where to move the files based on what the files' names say.
for file in file_names:
    if "SS" in file and not os.path.exists((path + "SocialStudies/" + file)):
        shutil.move(path + file, path + "SocialStudies/" + file)
    elif "Science" in file and not os.path.exists((path + "Science/" + file)):
        shutil.move(path + file, path + "Science/" + file)
    elif "Math" in file and not os.path.exists((path + "Math/" + file)):
        shutil.move(path + file, path + "Math/" + file)
    elif "Social Studies" in file and not os.path.exists((path + "SocialStudies/" + file)):
        shutil.move(path + file, path + "SocialStudies/" + file)
    elif "science" in file and not os.path.exists((path + "Science/" + file)):
        shutil.move(path + file, path + "Science/" + file)
    elif "math" in file and not os.path.exists((path + "Math/" + file)):
        shutil.move(path + file, path + "Math/" + file)
    elif "social studies" in file and not os.path.exists((path + "SocialStudies/" + file)):
        shutil.move(path + file, path + "SocialStudies/" + file)
    elif "Social studies" in file and not os.path.exists((path + "SocialStudies/" + file)):
        shutil.move(path + file, path + "SocialStudies/" + file)
    elif "socialstudies" in file and not os.path.exists((path + "SocialStudies/" + file)):
        shutil.move(path + file, path + "SocialStudies/" + file)
    elif "Socialstudies" in file and not os.path.exists((path + "SocialStudies/" + file)):
        shutil.move(path + file, path + "SocialStudies/" + file)
    elif "social Studies" in file and not os.path.exists((path + "SocialStudies/" + file)):
        shutil.move(path + file, path + "SocialStudies/" + file)