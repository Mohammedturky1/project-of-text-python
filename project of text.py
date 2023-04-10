#!/usr/bin/env python
# coding: utf-8

# In[28]:


import tkinter as tk 
from tkinter import *
from tkinter import messagebox, filedialog
import os
from pyarabic.number import text2number
from pyarabic.araby import strip_tashkeel
def createWidgets():
    global textArea
    textArea = Text(root)
    textArea.grid(sticky = N+E+S+W)
    
    menuBar = Menu(root)
    root.config(menu=menuBar)
    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="ملف جديد",command=newFile)
    fileMenu.add_command(label="فتح",command=openFile)
    fileMenu.add_command(label="حفظ",command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="خروج",command=Exit)
    menuBar.add_cascade(label="ملف ",menu=fileMenu)
    
    editMenu = Menu(menuBar, tearoff=0)
    editMenu.add_command(label="قص",command=cut)
    editMenu.add_command(label="نسخ",command=copy)
    editMenu.add_command(label="لصق",command=paste)
    menuBar.add_cascade(label="تعديل",menu=editMenu)

    editMenu = Menu(menuBar, tearoff=0)
    editMenu.add_command(label="num to text",command="")
    editMenu.add_command(label="text to num",command=texttonum)
    menuBar.add_cascade(label="الاعداد",menu=editMenu)
    
    editMenu = Menu(menuBar, tearoff=0)
    editMenu.add_command(label="حذف الحركات",command=tashkeel)
    editMenu.add_command(label="حذف التطويل ",command="")
    menuBar.add_cascade(label="اللغة العربية",menu=editMenu)
    
def newFile():
    global textArea
    root.title("Untitled - Notepad")
    file = None
    textArea.delete(1.0,END)
    
def openFile():
     global textArea
     file =filedialog.askopenfile(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")]) 
     file=file.name
        
     if file=="":
        file=None
     else:
        root.title(os.path.basename(file)+"- Notepad")
        textArea.delete(1.0,END)
        file=open(file,"rb")
        textArea.insert(1.0,file.read())
        file.close()
def saveFile():
    global textArea,file
    if file == None:
        file=filedialog.asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")]) 
        if file==None:
            file=None
        else:
            file = open(file,"w")
            file.write(textArea.get(1.0,END))
            file.close()
            file=file.name
            root.title(os.path.basename(file)+"_Notepade")
    else:
        file = open(file,"w")
        file.write(textArea.get(1.0,END))
        file.close()
def Exit():
    root.destroy()
def cut():
    global textArea
    textArea.event_generate("<<Cut>>")
def copy():
    global textArea
    textArea.event_generate("<<Copy>>")
def paste():
    global textArea
    textArea.event_generate("<<Paste>>")
def texttonum():
    
    global textArea
    textArea.event_generate("<<TEXT2NUMBER>>")

def tashkeel():
    global textArea
    textArea.event_generate("<<STRIP_TASH>>")
    print(strip_tashkeel(text))

root =tk.Tk()
root.title("new for me -my Notepad")
file = None


createWidgets()

root.mainloop()


# In[27]:


from pyarabic.number import text2number

print(text2number("عشرة"))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




