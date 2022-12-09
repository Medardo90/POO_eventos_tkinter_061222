# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 10:48:44 2022

@author: lab
"""

from tkinter import *
from tkinter import messagebox

def move_button():
    pass

def press_button():
    messagebox.showinfo("titulo", "ganaste")

root = Tk()
root.title("Game")
root.geometry("200x200")

Button(root, text ="Press me",command = press_button).place(x = 70,y = 20)


root.mainloop()