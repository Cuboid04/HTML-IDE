from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os
from tkinter import filedialog
root=Tk()
root.title("HTML IDE")
root.minsize(650,650)
root.maxsize(650,650)
root.configure(background="grey87")

open_img=ImageTk.PhotoImage(Image.open("open.png"))
run_img=ImageTk.PhotoImage(Image.open("run.png"))
save_img=ImageTk.PhotoImage(Image.open("save.png"))

file_name_lbl=Label(root, text="File Name : ")
file_name_lbl.place(relx=0.28, rely=0.03, anchor=CENTER)

file_name_input=Entry(root)
file_name_input.place(relx=0.46, rely=0.03, anchor=CENTER)

text_area=Text(root, height=35,width=80, bg="gray88")
text_area.place(relx=0.5, rely=0.55, anchor=CENTER)

name=""
def openfile():
    global name
    file_name_input.delete(0, END)
    text_area.delete(1.0, END)
    open_file=filedialog.askopenfilename(title="Open Text", filetypes=(("html Files", "*.html"),))
    name=os.path.basename(open_file)
    formatted_name=name.split('.')[0]
    file_name_input.insert(END, formatted_name)
    root.title(formatted_name)
    open_file=open(name, 'r')
    file=open_file.read()
    text_area.insert(END, file)
    open_file.close()


open_btn=Button(root, image=open_img, text="Open", command=openfile)
open_btn.place(relx=0.05, rely=0.03, anchor=CENTER)

save_btn=Button(root, image=save_img, text="Run")
save_btn.place(relx=0.11, rely=0.03, anchor=CENTER)

run_btn=Button(root, image=run_img, text="run")
run_btn.place(relx=0.17, rely=0.03, anchor=CENTER)

root.mainloop()