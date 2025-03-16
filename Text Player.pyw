from tkinter import *
import random
import pathlib
import time

time_change_text = 5
time_active = 10

def myloop():
    global last_active
    if time.time() - last_text > time_change_text:
        change_text()
    if root.state() == "normal":
        last_active = time.time()
    if time.time() - last_active > time_active:
        root.deiconify()
    root.after(1000, myloop)

def frame_click(event):
    change_text()


def on_window_resize(event):
    change_size()

def change_text():
    global last_text
    last_text = time.time()
    mylabel.config(text=random.choice(text).replace("\n", "").replace("\t", "\n"))
    change_size()

def change_size():
    myratio = max(mylabel.winfo_width() / root.winfo_width(), mylabel.winfo_height() / root.winfo_height())
    if myratio > 1.05 or myratio < 0.95:
        new_size = int(float(mylabel.cget("font").split(" ")[1]) / myratio)
        mylabel.config(font=("Arial", new_size))

root = Tk()
root.geometry("1200x100")
root.title("")
root.attributes("-topmost", True)
root.bind("<Configure>", on_window_resize)
mylabel = Label(root, text="", font=("Arial", 100))
mylabel.bind("<Button-1>", frame_click)
mylabel.place(relx=0.5, rely=0.5, anchor="center")
text = open(str(pathlib.Path(__file__).parent.resolve()) + "\\mytext.txt", "r", encoding="utf-8").readlines()
change_text()
last_text = time.time()
last_active = time.time()
myloop()
root.mainloop()