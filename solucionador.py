from tkinter import *
from tkinter.ttk import Separator


class gui():
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Resolvedor de Sudokus")
        self.ventana.resizable(False, False)

        self.casillas = []
        for i in range(9):
            self.casillas.append([])
            fr = Frame(self.ventana, highlightbackground="black", highlightcolor="black", highlightthickness=1)
            fr.grid(row=int(i / 3), column=int(i % 3))
            for j in range(3):
                for h in range(3):
                    valor = StringVar()
                    casilla = Entry(fr, width=4, textvariable=valor)
                    casilla.grid(row=j, column=h, sticky='nesw')
                    self.casillas[i].append(valor)
        btn_calcular = Button(self.ventana, text='Calcular', bg='cyan', command=lambda: solucionar(self.casillas))
        btn_calcular.grid(column=2, row=9, sticky='nesw')

        self.resultado = StringVar()
        lbl = Label(self.ventana, textvariable=self.resultado)
        lbl.grid(column=0, row=9, columnspan=2)

    def obtener_variables(self):
        return self.casillas


    def temenos_resultado(self, resultado):
        self.resultado.set(resultado)

#Recibe un array de casillas
#Usa variable global ventana_gui para notificar los resultados
def solucionar(casillas):
    fijas = []
    for cuadrado in casillas:
        for c in cuadrado:
            casilla = c.get()
            if casilla != "":
                try:
                    num = int(casilla)
                except ValueError:
                    ventana_gui.temenos_resultado("Valores no válidos")
                    return
                if num > 9 or num <= 0:
                    ventana_gui.temenos_resultado("Valores no válidos")
                    return
                #Valor válido:
                fijas.append(c)
    #iniciamos proceso de solucionado
    for cuadrado in casillas:
        for c in cuadrado:
            casilla = c.get()
            if casilla == "":
                c.set("1")
            elif fijas.__contains__(c):
                #Es de las fijas, la saltamos
                break
            elif int(casilla) < 9:
                #Aumentar el valor de la casilla
                c.set(str(int(casilla)+1))


    ventana_gui.temenos_resultado("Solucionado")


root = Tk()
ventana_gui = gui(root)

root.mainloop()
