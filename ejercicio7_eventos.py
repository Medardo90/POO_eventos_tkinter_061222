# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 09:29:36 2022

@author: lab
"""

import tkinter as tk 
root = tk.Tk()
txt = tk.Entry( root, text ="cargando.....")
lb1 = tk.Label(root, text ="text")

def changeColor(event):
    lb1.configure(bg="green")
    print( "liberado ",event.keysyn)
def changeColor2(event):
    lb1.configure(bg="blue")
    print("presionando ", event.keysyn)
    
txt.bind("<KeyRelease Down>", changeColor)
txt.bind("<KeyPress Down>", changeColor2)

txt.bind("<KeyRelease Return>", changeColor2)

txt.bind("<Control Alt_L>",lambda e: print("presionado control+alt"))
txt.grid()
txt.grid()
root.mainloop()