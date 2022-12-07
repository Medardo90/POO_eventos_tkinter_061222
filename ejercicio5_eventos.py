# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 10:00:02 2022

@author: lab
"""

from tkinter import *

def PressAnyKey (label):
    value = label.char
    print(value, "key is preset")
    
base = Tk()
base.geometry("300x150")
base.bind("<Key>",PressAnyKey)
mainloop()