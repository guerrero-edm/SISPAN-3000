from importlib.metadata import entry_points
from re import X
import tkinter as tk
from tkinter.messagebox import YES
from tkinter import ttk
import random
import mysql.connector

#Clases del Sistema: ----------------------------------------------------------
class Producto:
    def __init__(self,nombre,tipo="Pan",precio=0,existencia=0,db=None):
        self.ID = random.randint(4,100)
        self.__Nombre = str(nombre)
        self.__Tipo = str(tipo)
        self.__Precio = int(precio)
        self.__Existencia = int(existencia)
        if(db!=None):
            Cursor = db.cursor()
            Cursor.execute("INSERT INTO Productos VALUES ("+str(self.ID)+",'"+str(self.__Nombre)+"',"+str(self.__Precio)+",'"+str(self.__Tipo)+"',"+str(self.__Existencia)+")")
            db.commit()
        
    def Modificar_Ex(self,No):
        if (self.__Existencia == self.__Existencia + No) >= 0:
            self.__Existencia = self.__Existencia + No
        else:
            self.__Existencia = 0
            print("Ya no hay elementos que quitar")#Se cambia por la Interfaz
            
    def Establecer_Precio(self,Num):
        self.__Precio=Num
        
    def Devolver_Existencia(self):
        return self.__Existencia
    
    def Devolver_Precio(self):
        return self.__Precio
    
    def Devolver_Nombre(self):
        return self.__Nombre
    
    def Devolver_Tipo(self):
        return self.__Tipo
    
    def Borrar(self):
        #Agregar modificación base de datos--------------------------------------------------------------------
        pass
        

class Inventario: 
    def __init__(self,db,lista_p=[]):
        self.__productos = lista_p
        self.__Total_P = len(self.__productos) 
        self.__BD = db
        
    def Agregar_E_P(self,nombre,existencia):
        for x in self.__productos:
            if x.Nombre == nombre:
                x.Modificar_Ex(existencia)
                #Agregar modificación base de datos--------------------------------------------------------------------
            else:
                print("No encontrado") #Nota, se necesita cambiar a Interfaz
            
    def Quitar_E_P(self,nombre,existencia):
        for x in self.__productos:
            if x.Nombre == nombre:
                x.Modificar_Ex(-existencia)
                #Agregar modificación base de datos--------------------------------------------------------------------
            else:
                print("No encontrado") #Nota, se necesita cambiar a Interfaz
    
    def Crear_P(self,Nombre,Tipo,Precio):
        self.__productos.append(Producto(Nombre,Tipo,Precio,0,self.__BD))
    
    def Eliminar_P(self,nombre):
        for x in self.__productos:
            if x.Devolver_Nombre == nombre:
                #Agregar Dropeo de la base de datos -------------------------------------------------------------------
                self.__productos.pop(x)
                del x
                
    def Acceder_Producto(self,producto):
        lista=[str(producto.ID), str(producto.Devolver_Nombre()),str(producto.Devolver_Precio()),str(producto.Devolver_Tipo()),str(producto.Devolver_Existencia())]
        return lista
    
    def Acceder_Productos(self):
        return self.__productos        
      
class Pago:
    def __init__(self,db,Id_venta,cobro=0,pago=0,fecha="0/0/0",hora="0:00"):
        self.__Cobro = int(cobro)
        self.__Pago = int(pago)
        self.__Fecha = str(fecha)
        self.__Hora = str(hora)
        self.__ID_Venta = int(Id_venta)
        Cursor = db.cursor()
        Cursor.execute("INSERT INTO Pago VALUES ("+str(self.__Cobro)+","+str(self.__Pago)+","+"CURRENT_DATE()"+","+"CURRENT_TIME()"+","+str(self.__ID_Venta)+")")
        db.commit()
    
    def Borrar(self):
        #Agregar Dropeo de la base de datos----------------------------------------------------------------------------------------
        pass
    
    
class Venta:
    def __init__(self,db,fecha,hora,Productos = 0):
        self.__ID_V = random.randint(1,1000)
        self.__Fecha = str(fecha)
        self.__Hora = str(hora)
        self.__Prods = int(Productos)
        self.__Db = db
        Cursor = db.cursor()
        Cursor.execute("INSERT INTO Venta VALUES ("+str(self.__ID_V)+","+"CURRENT_DATE()"+","+str(self.__Prods)+",'"+"No"+"',"+"CURRENT_TIME()"+")")
        db.commit()
      
    def Pagar(self,cobro=0,pago=0):
        self.__Pago=Pago(self.__Db,self.__ID_V,cobro,pago,self.__Fecha,self.__Hora)
         
    def Cancelar_Venta(self):
        #Agregar Dropeo de la base de datos......................................................................................
        pass
    
    def Do_Devolucion(self,inventario,nombre):
        self.inventario.Agregar_E_P(nombre,existencia=1)

#funciones del sistema: 

def Iniciar_Inventario(db,lista_productos=[]):
    sql = "SELECT * FROM Productos"
    Cursor = db.cursor()
    Cursor.execute(sql)
   
    lista_filas = Cursor.fetchall()
    for x in lista_filas:
        print(x)
        (ID,Nombre,Precio,Tipo,Existencia)=x
        lista_productos.append(Producto(Nombre,Tipo,Precio,Existencia))
    return lista_productos

def Realizar_Venta(db,lista_Venta):
    pass
            
    

#Aqui empieza el Main --------------------------------------------------------

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="EEdmundoGueZ_935",
  database="syspan"
)

lista_Productos = Iniciar_Inventario(mydb)
Inventario1 = Inventario(mydb,lista_Productos)
lista_Ventas = []

Inventario1.Crear_P("Bolillo","Corgi",20000) #-----------------------CAMBIAR CADA QUE SE EJECUTE------------------------------------------

sql = "SELECT * FROM Productos"
micursor = mydb.cursor()
micursor.execute(sql)
lista_filas = micursor.fetchall()

#Interfaz-----------------------------------------------------------------------

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

tabla.heading('Nombre',text='ID')
tabla.heading('Tipo',text='Nombre')
tabla.heading('Precio',text='Precio')
tabla.heading('Existencia',text='Tipo')

productos = [('Dona', 'Pan yo creo', '6.66', 'Ni hay'),
            ('Concha', 'Sepa', 'Gratis pa', 'Creo')]

for i in lista_filas:
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

print("termine")