from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
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

open_btn=Button(root, image=open_img, text="Open")
open_btn.place(relx=0.05, rely=0.03, anchor=CENTER)

save_btn=Button(root, image=save_img, text="Run")
save_btn.place(relx=0.11, rely=0.03, anchor=CENTER)

run_btn=Button(root, image=run_img, text="run")
run_btn.place(relx=0.17, rely=0.03, anchor=CENTER)

root.mainloop()