# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 09:35:31 2022

@author: lab
"""

import tkinter as tk
raiz = tk.Tk()
def msg(pepitodelospalotes):
    print("hola estoy dentro del evento")
    lb1.config(text= "poo p61 ") 
    

btn1 = tk.Button(raiz, text="aceptar")
lb1 = tk.Label(raiz, text="texto cualquiera")



btn1.pack()
lb1.pack()

# btn1.bind("<Button-1>",msg)
# ejemplo lamda

btn1.bind("<Button-1>",lambda e:lb1.config(text="un clik left"))
btn1.focus()
btn1.bind("<Return>",lambda e:lb1.config(text="un enter")) #funciona con el enter        
raiz.mainloop()