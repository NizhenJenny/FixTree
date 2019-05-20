import json
import os


def create(PATH, fileName):
    # os.system("gumtree parse "+PATH+"old_"+fileName + " >" + PATH+"old_"+fileName+".json")


    # os.system("gumtree parse "+PATH+"new_"+fileName + " >" + PATH+"new_"+fileName+".json")

    os.system("gumtree diff "+PATH+"old_"+fileName + " "+ PATH+"new_"+fileName + " >" + PATH+"diffScript_"+fileName + ".txt")

    # os.system()



input_file = "D:\\reallyBug\\"
with open("output.json", "r") as f:
    j = json.load(f)
print(j)
for i,v in j.items():

    for bugInfo in v:
        inPATH = input_file + bugInfo["bugID"] + '\\'
        # print(inDir)
        key_file = bugInfo["FileName"][0]
        print(inPATH,"!!!!!!!!!!!!!!!!!!!!!!!!!")
        create(inPATH, key_file)
        print(key_file)


