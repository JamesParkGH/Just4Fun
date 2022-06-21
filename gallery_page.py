import glob
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from subprocess import call

def open_gallery_win():
    gallery_win = Tk()
    gallery_win.title('Gallery Window')
    gallery_win.geometry("800x500")
    gallery_win.resizable(0, 0)

    panel = tk.Label(gallery_win)
    panel.pack()

    path = "images_to_show/*.*"
    images = glob.glob(path)

    list1 = []

    global counter
    counter = -1
    
    for name in glob.glob(path):
        list1.append(name)

    text = tk.StringVar()
    text.set(list1[counter])
    label = Label(textvariable=text)
    label.pack()
    
    def inc_count():
        global counter
        counter += 1
        if counter == len(list1):
            counter = 0
        next_pic(counter)
        print_pic_name()

    def dec_count():
        global counter
        counter -= 1
        if -counter == len(list1):
            counter = 0
        previous_pic(counter)
        print_pic_name()

    def next_pic(counter):

        try:
            img = list1[counter]
        except StopIteration:
            return

        img = Image.open(img)
        resized_img = img.resize((640, 360))
        img = ImageTk.PhotoImage(resized_img)

        panel.img = img
        panel['image'] = img

    def previous_pic(counter):
        ab = list1[counter]
        img = Image.open(ab)
        resized_img = img.resize((660, 440))
        img = ImageTk.PhotoImage(resized_img)

        panel.img = img
        panel['image'] = img


    def return_menu():
        gallery_win.destroy()
        call(["python", "start_page.py"])

    def print_pic_name():
        a = (str(list1[counter]))
        sliced = a[15:-4]
        text.set("The name of the image is: " + sliced)

    next_pic_btn = tk.Button(text='Next Picture', command=inc_count)
    previous_pic_btn = tk.Button(text='Previous Picture', command=dec_count)
    return_menu_btn = Button(
        text='Return to Main Menu', command=return_menu)

    next_pic_btn.pack()
    previous_pic_btn.pack()
    return_menu_btn.pack()

    inc_count()

    gallery_win.mainloop()

open_gallery_win()