# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 10:18:31 2022

@author: lab
"""

import tkinter as tk
raiz = tk.Tk()
def msg(pepitodelospalotes):
    print("hola estoy dentro del evento")
    lb1.config(text= "poo p61 ") 
    

btn1 = tk.Button(raiz, text="aceptar")
lb1 = tk.Label(raiz, text="un lb1")
lb2 = tk.Label(raiz, text="un lb2")
lb3 = tk.Label(raiz, text="un lb3")



btn1.pack()
lb1.pack()
lb2.pack()
lb3.pack()

# btn1.bind("<Button-1>",msg)
# ejemplo lamda

btn1.bind("<Button-1>",lambda e:lb1.config(text="un clik left"))
lb2.focus()
lb2.bind("<Return>",lambda e:lb1.config(text="un enter en LB2")) #funciona con el enter        
raiz.mainloop()