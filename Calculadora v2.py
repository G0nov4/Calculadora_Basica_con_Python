from tkinter import *
# creamos
root = Tk()

root.title('Calculadora')
root.resizable(False,False)
root.geometry('400x290')
Label(root, text='Calculadora',bg ='#2B580C',fg='#F5EAEA', font=('Cambria',30),width='150',height='0').pack()
miFrame=Frame(root, width='600',height='400',bg='#639A67')
miFrame.pack()
#miFrame.config(bg='#5B5656', width='650',height='300')
numero_1 = StringVar()
numero_2 = StringVar()
Resultado = StringVar()


Entry(miFrame,width='12',textvariable = numero_1, justify='center').place(x='10',y='20')
Entry(miFrame,width='12',textvariable = numero_2, justify='center').place(x='130',y='20')
Label(miFrame, text=' = ',bg ='#639A67',fg='#F5EAEA',justify='center').place(x='240',y='20')
Entry(miFrame, textvariable=Resultado  , width='13',justify='center').place(x='270',y='20')

Label(miFrame, text=' Numero 1 ',bg ='#639A67',fg='#F5EAEA',justify='center').place(x='28',y='45')
Label(miFrame, text=' Numero 2 ',bg ='#639A67',fg='#F5EAEA',justify='center').place(x='140',y='45')
Label(miFrame, text=' Resultado ',bg ='#639A67',fg='#F5EAEA',justify='center').place(x='290',y='45')
def suma():
    a = int(numero_1.get())
    b = int(numero_2.get())
    Resultado.set(str((a+b)))
def resta():
    a = int(numero_1.get())
    b = int(numero_2.get())
    Resultado.set(str((a-b)))
def multiplicacion():
    a = int(numero_1.get())
    b = int(numero_2.get())
    Resultado.set(str((a*b)))
def divicion():
    a = int(numero_1.get())
    b = int(numero_2.get())
    Resultado.set(str((a/b)))
Button(miFrame, text='Suma', command=suma , width='20',height='3',bg='#D8EEB5').place(x='5',y='70')
Button(miFrame, text='Resta',command=resta , width='20',height='3', bg='#D8EEB5').place(x='205',y='70')
Button(miFrame, text='Multiplicacion',command=multiplicacion , width='20',height='3', bg='#D8EEB5').place(x='5',y='135')
Button(miFrame, text='Division',command=divicion , width='20',height='3', bg='#D8EEB5').place(x='205',y='135')
Button(miFrame, text='exit', width='15',height='0', command=root.destroy).place(x='115',y='200')
root.mainloop()