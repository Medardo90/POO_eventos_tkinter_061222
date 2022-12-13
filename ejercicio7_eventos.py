# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 02:05:58 2022

@author: Pablo Estrada
"""

import tkinter as tk 

# from modeloEdf import Ordenacion
# from vistaEdf import View

class Controller:
    def __init__(self):
        self.root= tk.Tk()
        self.model = Ordenacion 
        self.view = View(self.root , self.model)
        
    def run(self):
        self.root.title("Tkinter Mvc example")
        self.root.mainloop()
            
###################################################################

class Ordenacion:
    
    def ordenList(self,dictionaryData):
        print("ordenado......")
        ordenados = sorted(dictionaryData, key=lambda item : item["apellido"])
        print(ordenados)
        return ordenados 
    
###############################################################################

import tkinter as tk

class View():
    def __int__(self, root, model):
        self.model = model
        
        self.frame = tk.Frame(root)
        
        self.nombre= tk.StringVar()
        self.apellido = tk.StringVar()
        self.buscar = tk.StringVar()
        
        self.e1 = tk.Entry(root,textvarible=self.nombre, font=("Arial",14))
        self.e2 = tk.Entry(root,textvarible=self.apellido, font=("Arial",14))
        self.e3 = tk.Entry(root,textvarible=self.buscar, font=("Arial",12))
        
########################################################################################3
        
        b1= tk.Button(root,text= "Agregar")
        b2= tk.Button(root,text= "Reporte", command= self.reportes)
        b3= tk.Button(root,text= "Busqueda", command= self.reportes2)
        
        b1.bind("<Button 1>", self.agregarDatos)
        self.label= tk.label(root)
        
        
        self.e1.pack()
        self.e2.pack()
        
        b1.pack()
        b2.pack()
        self.e3.pack()
        b3.pack()
        self.label.pack()
        self.frame.pack()
        
        self.datos = []
    
    def agregarDatos(self,event):
        self.nombre = self.e1.get()
        self.apellido = self.e2.get()
        self.datos.append({"nombre": self.nombre, "apellido": self.apellido})
        print("datos ingresados")
        self.e1.delete(0,"end")
        self.e2.delete(0,"end")
        print(self.datos)

if __name__=="__main__":
    controler = Controller()
    controler.run
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        