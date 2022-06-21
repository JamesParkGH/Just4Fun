from tkinter import *
import tkinter as tk
import tkinter.font as font
from subprocess import call

def open_start_win():
    start_win = Tk()
    start_win.title('Start Window')
    start_win.geometry("400x300")
    start_win.resizable(0, 0)

    panel = tk.Label(start_win)
    panel.pack()

    def gallery_page():
        start_win.destroy()
        call(["python", "gallery_page.py"])
    
    def exit_win():
        start_win.destroy()

    gallery_btn = tk.Button(text='Open Gallery', bg='blue', fg='#ffffff', command=gallery_page)
    diff_font = font.Font(family='Helvetica', size=15, weight='bold')

    gallery_btn.config(height = 5, width = 20)
    exit_btn = tk.Button(text='Exit', command=exit_win)
    gallery_btn['font'] = diff_font
    gallery_btn.pack()
    exit_btn.place(x=180, y=200)

    start_win.mainloop()

open_start_win()