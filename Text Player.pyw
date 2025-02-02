from tkinter import *
import random
import pathlib
import time

time_change_text = 3
time_active = 10

def myloop():
    global last_active
    if time.time() - last_text > time_change_text:
        change_text()
    if root.state() == 'normal':
        last_active = time.time()
    if time.time() - last_active > time_active:
        root.deiconify()
    root.after(1000,myloop)

def frame_click(event):
    change_text()

def change_text():
    global last_text
    last_text = time.time()
    mylabel.config(text = random.choice(text).replace('\n','').replace('\t','\n'))

root = Tk()
root.geometry("375x875")
root.title("")
root.attributes('-topmost', True)
mylabel = Label(root, text = "",font=("Arial", 200))
mylabel.bind('<Button-1>', frame_click)
mylabel.place(relx=.5, rely=0.5, anchor="center")
text = open(str(pathlib.Path(__file__).parent.resolve()) + '\\mytext.txt', 'r', encoding='utf-8').readlines()
change_text()
last_text = time.time()
last_active = time.time()
myloop()
root.mainloop()