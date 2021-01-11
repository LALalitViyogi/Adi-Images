import tkinter as tk
from tkinter import ttk,messagebox
from tkinter import scrolledtext as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ImageScrapper import ImageScraper
import os

class imagescrape():
 def __init__(self):
  self.main_application = tk.Tk()
  self.main_application.geometry('450x350')
  self.main_application.title("Adi-Images")
  self.main_application.resizable(0,0)
  self.webdriver_path = os.getcwd()+"\\webdriver\\chromedriver.exe"
  self.image_path = os.getcwd()+"\\photos"
  self.min_resolution = (100,100)
  self.headless=False
  self.max_resolution=(1920,1080)
  self.data=dict()
  self.title_frame=ttk.LabelFrame(self.main_application, text='Adi-Image-Scrapping')
  self.title_frame.pack(pady=50)
  ## Labels
  self.tag_label=ttk.Label(self.title_frame,text='Query Name')
  self.num_label=ttk.Label(self.title_frame,text='Image Number')

  ## Entry
  self.tag_entry=ttk.Entry(self.title_frame,width=30)
  self.num_entry=ttk.Entry(self.title_frame,width=30)

  ## textArea
  self.text_area=st.ScrolledText(self.title_frame,wrap=tk.WORD,width=25,height=5,font = ("Times New Roman",10))
  self.text_area.grid(row=4,column=1)
  self.text_area.configure(state='disabled')
  
  #buttons
  self.addtag_button=ttk.Button(self.title_frame, text='Add Tag',command=self.addtag)
  self.search_button=ttk.Button(self.title_frame, text='Scrap Now!',command=self.search)
  self.reset_button=ttk.Button(self.title_frame, text='Reset',command=self.reset)
  
  # Griding
  self.tag_label.grid(row=0,column=0,padx=5,pady=5)
  self.tag_entry.grid(row=0,column=1,padx=5,pady=5)
  self.num_label.grid(row=1,column=0,padx=5,pady=5)
  self.num_entry.grid(row=1,column=1,padx=5,pady=5)
  
  self.addtag_button.grid(row=2,column=0,padx=5,pady=5)
  self.search_button.grid(row=2,column=1,padx=5,pady=5)
  self.reset_button.grid(row=3,column=0,padx=5,pady=2)
  
  self.main_application.mainloop()

 def search(self):
   search_keys=list(self.data.keys())
   for search_key in search_keys:
     number_of_images=int(self.data[search_key])
     image_scrapper = ImageScraper(self.webdriver_path,self.image_path,search_key,number_of_images,self.headless,self.min_resolution,self.max_resolution)
     image_urls = image_scrapper.find_image_urls()
     image_scrapper.save_images(image_urls)
   
   return messagebox.showwarning("Download Completed","Congratulations, All Images Are Saved") and self.reset()
 
 def reset(self):
  self.tag_entry.delete(0,tk.END)
  self.num_entry.delete(0,tk.END)
  self.data.clear()
  self.text_area.configure(state='normal')
  self.text_area.delete(1.0,tk.END)
  self.text_area.configure(state='disabled')

 def addtag(self):
  try:
   if len(self.tag_entry.get())==0:
    return messagebox.showwarning("Warning","Tag Cannot Be Blanked")
   else:
    self.data[self.tag_entry.get()]=int(self.num_entry.get())
    self.text_area.configure(state='normal')
    self.text_area.delete(1.0,tk.END)
  except:
   return messagebox.showwarning("User Error","Please Enter Valid Input")
  
  for i in range(len(self.data.keys())):
    key=list(self.data.keys())[i]
    self.text_area.insert(tk.INSERT,'"'+str(key)+'",')
  self.tag_entry.delete(0,tk.END)
  self.num_entry.delete(0,tk.END)
  self.text_area.configure(state='disabled')
if __name__ == "__main__":
 my=imagescrape()
 