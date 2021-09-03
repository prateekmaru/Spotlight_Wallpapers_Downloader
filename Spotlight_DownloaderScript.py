import tkinter as tk
import os,random,string,glob,shutil,tempfile,magic
from PIL import Image, ImageTk
from tkinter import ttk, messagebox

def fileDownload():
    if os.path.exists(r'{}\expertdotpy'.format(tempfile.gettempdir())): shutil.rmtree(r'{}\expertdotpy'.format(tempfile.gettempdir()))
    if not os.path.exists(r'{}\expertdotpy'.format(tempfile.gettempdir())): os.makedirs(r'{}\expertdotpy'.format(tempfile.gettempdir()))

    folderLocation = r"C:\Users\{}\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets".format(os.getenv('username'))
    for path, subdirs, files in os.walk(folderLocation):
        for name in files:
            if int(os.path.getsize(str(os.path.join(path, name)))) >= int('204800'):
                shutil.copy2(os.path.join(path, name), r'{}\expertdotpy\{}.{}'.format(tempfile.gettempdir(), ''.join(random.choices(string.ascii_letters + string.digits, k=20)), magic.from_file(os.path.join(path, name), mime = True).split('/')[1]) )
fileDownload()
#=================================== GUI Part ===================================#
root = tk.Tk()
root.geometry("1000x800")
root.configure(background='black')
root.title('Windows 10/11 Spotlight wallpaper downloader by @Expert.py @prateekmaru')
def downloadImage():
    try:
        for selected_item in lst.selection():
            item = lst.item(selected_item)
        item['values'][0]
        shutil.copy2(r"{}\expertdotpy\{}".format(tempfile.gettempdir(),item['values'][0]), r"C:\Users\{}\Pictures".format(os.getenv('username')))
        messagebox.showinfo('Downloaded', "Image saved successfully.\nCheck '\Pictures' folder")
    except:
        messagebox.showinfo('Error', "Error: Something went wrong ")
    
def showimg(e):
    for selected_item in lst.selection():
        item = lst.item(selected_item)
    img = Image.open(r"{}\expertdotpy\{}".format(tempfile.gettempdir(),item['values'][0]))
    img.thumbnail((600, 600), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    label.config(image=photo)
    label.image = photo

label1 = tk.Label(root, text="@prateekmaru credit : @expert.py",fg = "black",bg = "white",font=("Raleway", 10, "bold"))
label1.grid(row = 0, column = 0) 

label1 = tk.Label(root, text="Windows 10/11 Spotlight Wallpapers Downloader Note: After Download Check \Pictures Folder",fg = "white",bg = "black",font=("Raleway", 10, "bold"))
label1.grid(row = 0, column = 1,sticky='w') 

lst = ttk.Treeview(root, columns="FileName", show='headings')   
lst.heading('FileName', text='Select file')

Btn = tk.Button(root, text="Downlaod", command = downloadImage,bg='green', fg='white',font=("Raleway", 20, "bold"))
Btn.grid(row = 2, column = 0)

namelist = []
for path, subdirs, files in os.walk(r"{}\expertdotpy".format(tempfile.gettempdir())):
    for name in files:
        namelist.append(name)
        lst.insert('',tk.END, values=name)

lst.grid(row = 1, column = 0, pady='50')
lst.bind('<<TreeviewSelect>>', showimg)

im = Image.open( r"{}\expertdotpy\{}".format(tempfile.gettempdir(),namelist[0]))
im.thumbnail((600, 600), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(im)

label = tk.Label(root, image=photo)
label.grid(row = 1, column = 1, sticky='w',padx='40', rowspan=500)
label.img = photo  

root.mainloop()

