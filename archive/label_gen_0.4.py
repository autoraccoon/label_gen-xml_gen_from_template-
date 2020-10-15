# coding=utf-8
import os
import csv
import builtins
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from builtins import input

#________________________________________
#functions

def login(text):
    global log
    log.writelines(str(text)+"\r")

def create_dir(dirName):
    # Create output directory
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        login("Directory " + dirName +  " Created ")
    else:    
        login("Directory " + dirName +  " already exists")

def choose_output():
    messagebox.showinfo("Output", "Please choose where to output your files")
    root.filename =  filedialog.askdirectory()
    output = os.path.join(root.filename,template.split(".")[0])
    create_dir(output)
    return output

def choose_replace(): 
    messagebox.showinfo("Replacement list", "Please choose your .CSV replacement list")
    root.filename =  filedialog.askopenfilename()
    replacement_list = ""
    if check_type(root.filename,"csv"):
        replacement_list = root.filename
    else:
        messagebox.showwarning("Error", "Not a valid .CSV replacement list")
    return replacement_list
    
def  check_type(root,type):
    #type is .extension
    login ("testing file template:" +root)
    test = False
    if root.endswith("."+str(type)):
        test = True
    login(test)
    return test
    
#GUI funcitons
def replace_text():
    login("replace text in "+str(template))
    if template == "": messagebox.showwarning("Error", "No valid .SVG template selected")
    else:
        output = choose_output()
        replacement_list = choose_replace()
        with open(template,"r") as svg:
            with open(replacement_list,newline='') as replace_list:
            
                reader = csv.DictReader(replace_list,delimiter=';')
                login("Searching for replacement")

                #to be replaced list
                login("Replacing: "+str(reader.fieldnames))
                
                #look for replacement
                text = svg.read()
                i=0
                for row in reader:
                    i+=1
                    login("row is :"+str(row)+"\r")
                    for e in row: 
                        login("element is :"+str(e)+"\r")
                        #replacing
                        text = text.replace("%VAR_"+e+"%", row[e])
                        login("Replaced "+e+" by "+row[e])

                    #output
                    out = os.path.join(output,("output"+str(i)+".svg"))
                    login(out)
                    x = open(out,"w")
                    x.writelines(text)
                    x.close()

                print('text replacement complete')

def replace_color():
    login("replace color in "+str(template))
    if template == "": messagebox.showwarning("Error", "No valid .SVG template selected")
    else:
        output = choose_output()
        replacement_list = choose_replace()
        with open(template,"r") as svg:
            with open(replacement_list,newline='') as replace_list:
            
                reader = csv.DictReader(replace_list,delimiter=';')
                login("Searching for replacement")

                #to be replaced list
                login("Replacing: "+str(reader.fieldnames))
                
                #look for replacement
                text = svg.read()
                i=0
                for row in reader:
                    i+=1
                    login("row is :"+str(row)+"\r")
                    for e in row: 
                        login("element is :"+str(e)+"\r")
                        #replacing
                        text = text.replace("#"+e, row[e])
                        login("Replaced "+e+" by "+row[e])

                    #output
                    out = os.path.join(output,("output"+str(i)+".svg"))
                    login(out)
                    x = open(out,"w")
                    x.writelines(text)
                    x.close()

                print('Color replacement complete')

def select():
    global template
    print ("Please choose project SVG template")
    root.filename =  filedialog.askopenfilename()
    if  check_type(root.filename,"svg"):
        template = root.filename
    else:
        messagebox.showwarning("Error", "Not a valid .SVG template")

def cancel():
    log.close()
    quit()
    
def init_gui():
    #Tkinter GUI
    root = tk.Tk()
    root.title("Trend upgrade scanner")
    root.minsize(400,100)
    root.geometry("480x100")
    
    # create the main sections of the layout, 
    # and lay them out
    top = tk.Frame(root)
    bottom = tk.Frame(root)
    top.pack(side=tk.TOP)
    bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    # create the widgets for the top part of the GUI,
    # and lay them out
    s = tk.Button(root, text="Select template", wraplength=80, width=10, height=2, command=select)
    c = tk.Button(root, text="Leave", width=10, height=2, command=cancel)
    e = tk.Button(root, text="Replace text", wraplength=80, width=10, height=2, command=replace_text)
    r = tk.Button(root, text="Replace color", width=10, height=2, command=replace_color)
    s.pack(in_=top, side=tk.LEFT)
    e.pack(in_=top, side=tk.LEFT)
    r.pack(in_=top, side=tk.LEFT)
    c.pack(in_=top, side=tk.LEFT)

    # create the widgets for the bottom part of the GUI,
    # and lay them out
    global path
    path = tk.Label(root, text = "...", width=35, height=15)
    path.pack(in_=bottom, side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    w = tk.Label(root, text="Please choose SET Project file directory")
    w.pack()

    return root


#____________________________________________________________
#main code
global log
    
log = open("log.txt","w")

template = ""
root = init_gui()
root.mainloop()
