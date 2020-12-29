import tkinter as tk
from tkinter import ttk
from imagescrape import imagescrape
import tkinter.scrolledtext as st 
import pyttsx3
import os


main_application = tk.Tk()
main_application.geometry('400x300')
main_application.title("Adi-Images")
main_application.resizable(0,0)
title_frame=ttk.LabelFrame(main_application, text='Adi-Image-Scrapping')
title_frame.pack(pady=50)

# labels
tag_label=ttk.Label(title_frame,text='Query Name')
num_label=ttk.Label(title_frame,text='Image Number')

#entry box
tag_entry=ttk.Entry(title_frame,width=30)
num_entry=ttk.Entry(title_frame,width=30)

text_area = st.ScrolledText(title_frame,wrap   = tk.WORD, width =30 ,height = 5,font = ("Times New Roman",10))
text_area.grid(row=3, column =1, pady =5, padx =5)
text_area.configure(state='disabled')
#widget_functions
data=dict()
def addtag():
 global text_area
 global tag_entry
 global num_entry
 data[tag_entry.get()]=num_entry.get()
 text_area.configure(state='normal')
 text_area.delete(1.0,tk.END)

 for i in range(len(data.keys())):
  key=list(data.keys())[i]
  text_area.insert(tk.INSERT,'"'+str(key)+'",')
 
 tag_entry.delete(0,tk.END)
 num_entry.delete(0,tk.END)
 text_area.configure(state='disabled')
def searchit():
 pass

#buttons
addtag_button=ttk.Button(title_frame, text='Add Tag',command=addtag)
search_button=ttk.Button(title_frame, text='Scrap Now!',command=searchit)
#griding
tag_label.grid(row=0,column=0,padx=5,pady=5)
tag_entry.grid(row=0,column=1,padx=5,pady=5)

num_label.grid(row=1,column=0,padx=5,pady=5)
num_entry.grid(row=1,column=1,padx=5,pady=5)

addtag_button.grid(row=2,column=0,padx=5,pady=5)
search_button.grid(row=2,column=1,padx=5,pady=5)
main_application.mainloop()