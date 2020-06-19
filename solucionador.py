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

def comprobar_fila(tablero, nuevoValor, posicion):
    inicio_col = posicion - (posicion % 3)
    if int(posicion/9) == 0 or int(posicion/9) == 3 or int(posicion/9) == 6:
        inicio_col +=9
        if tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor or tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor+10:
            return False
        for i in range(2):
            inicio_col+=1
            if tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor or tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor+10:
                return False
        inicio_col += 7
        for i in range(2):
            inicio_col+=1
            if tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor or tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor+10:
                return False
        return True
    if int(posicion/9) == 1 or int(posicion/9) == 4 or int(posicion/9) == 7:
        inicio_col -= 9
        if tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor or tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor+10:
            return False
        for i in range(2):
            inicio_col+=1
            if tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor or tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor+10:
                return False
        inicio_col += 9 + 7
        if tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor or tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor+10:
            return False
        for i in range(2):
            inicio_col += 1
            if tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor or tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor+10:
                return False
        return True
    if int(posicion/9) == 2 or int(posicion/9) == 5 or int(posicion/9) == 8:
        inicio_col -=18
        if tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor or tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor+10:
            return False
        for i in range(2):
            inicio_col += 1
            if tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor or tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor+10:
                return False
        inicio_col += 7
        for i in range(2):
            inicio_col += 1
            if tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor or tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor+10:
                return False
        return True




def comprobar_columna(tablero, nuevoValor, posicion):
    inicio_col = (posicion % 3) + ((int(posicion / 9) % 3)*9) #Primer númeor de la columna
    if tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor or tablero[int(inicio_col / 9)][
        inicio_col % 9] == nuevoValor + 10:
        return False
    inicio_col += 3
    if tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor or tablero[int(inicio_col / 9)][
        inicio_col % 9] == nuevoValor + 10:
        return False
    inicio_col += 3
    if tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor or tablero[int(inicio_col / 9)][
        inicio_col % 9] == nuevoValor + 10:
        return False
    inicio_col += -6 + 27
    if tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor or tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor+10:
        return False
    inicio_col += 3
    if tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor or tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor+10:
        return False
    inicio_col += 3
    if tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor or tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor+10:
        return False
    inicio_col += -6 + 27
    if tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor or tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor+10:
        return False
    inicio_col += 3
    if tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor or tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor+10:
        return False
    inicio_col += 3
    if tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor or tablero[int(inicio_col / 9)][inicio_col % 9] == nuevoValor+10:
        return False
    return True



#Recibe un array de casillas
#Usa variable global ventana_gui para notificar los resultados
def solucionar(casillas):
    tablero = []
    for cuadrado in casillas:
        tablero.append([])
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
                tablero[len(tablero)-1].append(int(casilla)+10)
            else:
                tablero[len(tablero)-1].append(0)
    #iniciamos proceso de solucionado
    posicion = 0
    while posicion!=81:
        if tablero[int(posicion/9)][posicion % 9] < 9:
            nuevoValor = tablero[int(posicion / 9)][posicion % 9] + 1
            valido = True
            if tablero[int(posicion / 9)].__contains__(nuevoValor) or tablero[int(posicion / 9)].__contains__(nuevoValor + 10):
                #Mantenemos posicion. El nuevo valor no es válido
                posicion=posicion
                tablero[int(posicion / 9)][posicion % 9] = nuevoValor
                valido = False
            if not comprobar_fila(tablero, nuevoValor, posicion):
                posicion=posicion
                tablero[int(posicion / 9)][posicion % 9] = nuevoValor
                valido = False
            if not comprobar_columna(tablero, nuevoValor, posicion):
                posicion=posicion
                tablero[int(posicion / 9)][posicion % 9] = nuevoValor
                valido = False
            if valido:
                tablero[int(posicion / 9)][posicion % 9] = nuevoValor
                posicion += 1

        elif tablero[int(posicion/9)][posicion % 9] == 9:
            #Hay que ir para atrás
            tablero[int(posicion / 9)][posicion % 9] = 0
            while True:
                posicion -= 1
                if tablero[int(posicion / 9)][posicion % 9] < 9:
                    break
                elif not tablero[int(posicion / 9)][posicion % 9] > 10:
                    tablero[int(posicion / 9)][posicion % 9] = 0
                if posicion == 0:
                    ventana_gui.temenos_resultado("No tiene solucion")
                    return False
        elif tablero[int(posicion/9)][posicion%9] > 10:
            #Saltar al siguiente
            posicion += 1

    posicion=0
    for cuadrado in casillas:
        for c in cuadrado:
            if tablero[int(posicion / 9)][posicion % 9] > 9 :
                tablero[int(posicion / 9)][posicion % 9] -= 10
            c.set(str(tablero[int(posicion / 9)][posicion % 9]))
            posicion += 1
    ventana_gui.temenos_resultado("Solucionado")

root = Tk()
ventana_gui = gui(root)

root.mainloop()
