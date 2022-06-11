from importlib.metadata import entry_points
from re import X
import tkinter as tk
from tkinter.messagebox import YES
from tkinter import ttk

root = tk.Tk()
root.title('Inventario')


class Campo(tk.Frame):
    def __init__(self,padre,texto, ancho):
        tk.Frame.__init__(self,padre)
        label = tk.Label(self, text=texto)
        label.pack(side=tk.LEFT)
        entry = tk.Entry(self, width=ancho)
        entry.pack(side=tk.RIGHT)

columnas = ('Nombre', 'Tipo', 'Precio', 'Existencia')

frameTabla = tk.Frame(root)
frameTabla.pack(side=tk.BOTTOM)

tabla = ttk.Treeview(frameTabla, columns=columnas, show='headings')

tabla.heading('Nombre',text='Nombre')
tabla.heading('Tipo',text='Tipo')
tabla.heading('Precio',text='Precio')
tabla.heading('Existencia',text='Existencia')

productos = [('Dona', 'Pan yo creo', '6.66', 'Ni hay'),
            ('Concha', 'Sepa', 'Gratis pa', 'Creo')]

for i in productos:
    tabla.insert('', tk.END, values=i)


tabla.pack(side=tk.BOTTOM)

scrollbar = ttk.Scrollbar(frameTabla, orient=tk.VERTICAL, command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)
scrollbar.pack()

frameBusqueda = tk.Frame(root)
frameBusqueda.pack(side=tk.BOTTOM)
entryBusqueda = tk.Entry(frameBusqueda)
entryBusqueda.pack(side=tk.LEFT)
botonBusqueda = tk.Button(frameBusqueda, text="Buscar")
botonBusqueda.pack(side=tk.LEFT)

botonera = tk.Frame(root)
botonera.pack(side=tk.BOTTOM)
botonAgregar = tk.Button(botonera, text="Agregar")
botonAgregar.pack(side=tk.LEFT)
botonModificar = tk.Button(botonera, text="Modificar")
botonModificar.pack(side=tk.LEFT)
botonEliminar = tk.Button(botonera, text="Eliminar")
botonEliminar.pack(side=tk.LEFT)

frameFormulario = tk.Frame(root)
frameFormulario.pack(side=tk.BOTTOM)
frameNombre = Campo(frameFormulario, "Nombre",30)
frameNombre.pack(expand=tk.YES, fill=tk.X)
frameTipo = Campo(frameFormulario, "Tipo",30)
frameTipo.pack(expand=tk.YES, fill=tk.X)
framePrecio = Campo(frameFormulario, "Precio",30)
framePrecio.pack(expand=tk.YES, fill=tk.X)
frameExistencia = Campo(frameFormulario, "Existencia",30)
frameExistencia.pack(expand=tk.YES, fill=tk.X)

root.mainloop()