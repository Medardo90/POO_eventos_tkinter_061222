# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 09:29:36 2022

@author: lab
"""

import tkinter as tk 
root = tk.Tk()
txt = tk.Entry(root, text ="starting.....")
lbl = tk.Label(root, text ="text")

def changeColor(event):
    lbl.configure(bg="green")
    print( "liberando ",event.keysym)
def changeColor2(event):
    lbl.configure(bg="blue")
    print("presionando ", event.keysym)
    
txt.bind("<KeyRelease Down>",changeColor)
txt.bind("<KeyPress Down>", changeColor2)

txt.bind("<KeyPress Return>", changeColor2)

txt.bind("<Control Alt_L>",lambda e: print("presionado ctrl+alt"))

txt.grid()
lbl.grid()
root.mainloop()