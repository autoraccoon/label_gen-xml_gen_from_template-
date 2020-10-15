# coding=utf-8

#in and out with absolute path
input = "C:\Users\Francois\Desktop\Francois\Business\BandProvider\products\packaging\labels\cordes\templates\v1.svg"
output = "C:\Users\Francois\Desktop\Francois\Business\BandProvider\products\packaging\labels\cordes\templates\test_.svg"
csv = "C:\Users\Francois\Desktop\Francois\Business\BandProvider\products\packaging\labels\cordes\templates\items_list.csv"

offendant = "type"
replacer = "replaced"
#don't modify under this line
#________________________________________

#format files path
pathval = [input, output, csv]
for i in range(len(pathval)): 
    #print(pathval[i])
    pathval[i] = pathval[i].replace('\v','\\v')
    pathval[i] = pathval[i].replace('\t','\\t')
    #print(pathval[i])
    i = i+1

#search csv
replace_list = open(pathval[2], "r")
replace_list = ''.join([c for c in replace_list])
list_lines = replace_list.split("\n")

#to be replaces list
off_list = list_lines[0].split(";")

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
    out = pathval[1].split(".")
    out[0]=out[0]+case[0]
    out = out[0]+"."+out[1]
    print(out)
    x = open(out,"w")
    x.writelines(text)
    x.close()

    i=i+1
