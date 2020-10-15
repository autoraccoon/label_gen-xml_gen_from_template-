# coding=utf-8
import os
import builtins

from builtins import input

print("Make sure all the files are in the same folder as the app")

#in and out with absolute path
template = input("Enter template name: ")
output = "output"
csv = input("enter csv name containing info: ")

#don't modify under this line
#________________________________________


#format files path
pathval = [template, output, csv]
for i in range(len(pathval)): 
    pathval[i] = pathval[i].replace('\v','\\v')
    pathval[i] = pathval[i].replace('\t','\\t')
    i = i+1
#check for extensions in path
if pathval[0].__contains__("."):
     pathval[0] = pathval[0].split(".")
     pathval[0] = ''.join([c for c in pathval[0][0]])
pathval[0] = pathval[0]+".svg"
print("Template: "+pathval[0])
if pathval[2].__contains__("."):
     pathval[2] = pathval[2].split(".")
     pathval[2] = ''.join([c for c in pathval[2][0]])
pathval[2] = pathval[2]+".csv"
print("CSV: "+pathval[2])


#search csv
replace_list = open(pathval[2], "r")
replace_list = ''.join([c for c in replace_list])
list_lines = replace_list.split("\n")

#to be replaced list
off_list = list_lines[0].split(";")

	
# Create output directory
dirName = output
if not os.path.exists(dirName):
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ")
else:    
    print("Directory " , dirName ,  " already exists")

#look for replacement
i=1
while i < (len(list_lines)-1):
    #read template
    text = open(pathval[0], "r")
    text = ''.join([c for c in text])
        
    case = list_lines[i].split(";")
    #print(case)
    j = 0
    while j < len(off_list):
                   #case[j] = case[j].split("\n")
                   #print(case[j])
                   offendant = off_list[j]
                   replacer = case[j]
   
                   #replacing
                   text = text.replace("%VAR_"+offendant+"%", replacer)
                   #print(text)
                   #print(j)
                   j = j+1

    #output
    out = pathval[1]+"\\item_"+case[0]+".svg"
    print(out)
    x = open(out,"w")
    x.writelines(text)
    x.close()

    i=i+1

print('complete')
