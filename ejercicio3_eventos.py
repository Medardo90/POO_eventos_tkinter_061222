# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 10:23:09 2022

@author: lab
"""

import tkinter as tk
from tkinter import ttk 

def return_pressed(event):
    print("return key pressed")
    
def log(event):
    print(event)
    
def un_click(event):
    print("hola")
        
root = tk.Tk()

btn = ttk.Button(root,text="Save")
btn.bind("<Return>", return_pressed)
btn.bind("<Button-1>", un_click)

btn.bind("<Return>", log,add="+")

btn.focus()
btn.pack(expand=True)

root.mainloop()
