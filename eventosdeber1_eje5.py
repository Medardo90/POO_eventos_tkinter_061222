# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 10:49:21 2022

@author: lab
"""

from tkinter import *
from tkinter import messagebox
from random import randint

def move_button(evento):
    evento.widget.place(x = randint(0, 100), y = randint(0,100))

def press_button():
    messagebox.showinfo("titulo", "ganaste")

root = Tk()
root.title("Game")
root.geometry("200x200")

btn = Button(root, text ="Press me",command = press_button)
btn.place(x = 70,y = 20)
btn.bind("<Enter>", move_button)

root.mainloop()