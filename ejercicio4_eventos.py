# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 09:40:30 2022

@author: lab
"""

import tkinter as tk
raiz = tk.Tk()

def fun_msg(e):
    print("hola"+str(e.x))
def fun_msg2(e):
    print("hola, en el eje x "+str(e.x))
    print("hola, en el eje y :"+str(e.y))
    if e.x == 100 and e.y == 100:
        lb.config(bg ="red")
        
btn = tk.Button(raiz, text="aceptar todo")
lb= tk.Label(raiz, bg="yellow", text ="esto es un texto grande")
    
btn.pack()
lb.pack()

btn.bind("<Button-1>", fun_msg)
lb.bind ("<Motion>", fun_msg)   
raiz.bind("<Motion>", fun_msg2)
raiz.mainloop()