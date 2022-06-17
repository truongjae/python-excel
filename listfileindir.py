# from os import listdir
# from os.path import isfile, join
# mypath = "D:/"
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# print(onlyfiles)


# import glob

# txtfiles = []
# for file in glob.glob("E:/*"):
#     txtfiles.append(file)
# print(txtfiles)

import os

listimg = []
for r, d, f in os.walk("D:\\1"):
    for file in f:
        if file.endswith(".jpg") or file.endswith(".JPG"):
            listimg.append(os.path.join(r, file))
print(listimg)
for i in listimg:
	x = i.split("\\")
	x = x[len(x)-1]
	os.system("copy "+i+" D:\\hihi\\"+x)