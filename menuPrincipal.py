import tkinter as tk

menu = tk.Tk()
menu.title('Menu principal')
menu.resizable(False,False)

frameBotones = tk.Frame(menu, height=100)
frameBotones.pack(fill=tk.X, side=tk.TOP)

imagenPersonal = tk.PhotoImage(file="personal.png").subsample(2)
imagenInformes = tk.PhotoImage(file="reporte.png").subsample(2)
imagenInventario = tk.PhotoImage(file="inventario.png")
imagenVentas = tk.PhotoImage(file="ventas.png").subsample(6)

botonInventario = tk.Button(frameBotones, text="Inventario",image=imagenInventario,compound=tk.TOP,width=250,height=225).pack(side=tk.LEFT,fill=tk.BOTH)
botonVentas = tk.Button(frameBotones, text="Ventas",image=imagenVentas,compound=tk.TOP,width=250,height=225).pack(side=tk.LEFT,fill=tk.BOTH)
botonPersonal= tk.Button(frameBotones, text="Plantilla de personal",image=imagenPersonal,compound=tk.TOP,width=250,height=225).pack(side=tk.LEFT,fill=tk.BOTH)
botonInformes = tk.Button(frameBotones, text="Informes de inventario y ventas",image=imagenInformes,compound=tk.TOP,width=250,height=225).pack(side=tk.LEFT,fill=tk.BOTH)

frameInfo = tk.Frame(menu, bg='red').pack()
labelTitulo = tk.Label(frameInfo, text="Panaderia")
labelTitulo.pack()
labelTituloDos = tk.Label(frameInfo, text="Syspan - 3000")
labelTituloDos.pack()

imagenInfo = tk.PhotoImage(file="syspan.png").subsample(2)
tk.Label(frameInfo, image=imagenInfo).pack()
tk.Label(frameInfo, text="GARCIA JIMENEZ JUAN CARLOS").pack()
tk.Label(frameInfo, text="HERNÁNDEZ VÁZQUEZ ROGELIO").pack()
tk.Label(frameInfo, text="GUERRERO ZORZA ERICK EDMUNDO").pack()
tk.Label(frameInfo, text="ORTIZ CAMACHO LUIS ENRIQUE").pack()

menu.mainloop()
