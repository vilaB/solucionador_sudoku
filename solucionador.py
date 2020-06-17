from tkinter import *
from tkinter.ttk import Separator


class gui():
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Resolvedor de Sudokus")
        self.ventana.resizable(False, False)

        self.casillas=[]
        for i in range(9):
            self.casillas.append([])
            for j in range(9):
                valor = StringVar()
                casilla = Entry(self.ventana, width=4, textvariable=valor)
                casilla.grid(row=i, column=j, sticky='nesw')
                self.casillas[i].append([casilla, valor])




root = Tk()
ventana_gui = gui(root)
root.mainloop()