from tkinter import *
import os
import webbrowser
import sys
import conversiones as conv

sistemas = "sys"
memorias = "memorias"
operaciones = "operaciones"
botones = {"sys":{},"memorias":{},"operaciones":{},"menuInicial":{}}
display = "0"
sistema = ["DEC"] #el ultimo elemento de este array es el estado actual
sistemasDict = {"d":"DEC", "b":"BIN", "o":"OCT", "h":"HEX"}
banderaSistTemp = False
memoria = 0

def frame(ventana, lado, color="pale turquoise", width=0):
    w = Frame(ventana, width=width, bg=color)
    w.pack(side=lado, expand=YES, fill=BOTH)
    return w

def crear_boton(ventana, lado=TOP, relleno=BOTH, texto="", command=None, color="dark sea green"):
    btn = Button(ventana, text=texto, command=command, font = "Verdana 12", bg=color)
    btn.pack(side=lado, expand=YES, fill=relleno)
    return(btn)

def calcular(display):
    info = display.get()
    '''
    if not(info.isdigit()):
        temp = ""
        flag = False
        for i in info:
            if i in ("d","b","o","h"):
                flag = True
        #    while flag and i.isdigit():
    '''
    if info.count(".") > 1:
        display.set("Error.")
    if info[len(info)-1]==0:
        info = info[:len(info)-1]
    try:
        res = eval(info)
        display.set("{0} = {1} ".format(info, str(res)))
    except Exception as e:
        display.set("ERROR {0}".format(e))

def nada():
    filewin = Toplevel(principal)
    err = Label(filewin,fg="black",text="Error accesando a la aplicacion predeterminada para pdf.",font="Verdana 20")
    err.pack()

def abrirManual():
    try:
        if sys.platform == "linux":
            webbrowser.open_new(r'./manual_de_usuario_calculadora.pdf')
        else:
            os.startfile("manual_de_usuario_calculadora.pdf")
    except Exception as e:
        print(e)
        nada()

def operacionesMemoria(com):
    global memoria
    global display
    if com == "M+":
        memoria += int(display.get())
    elif com == "M-":
        memoria -= int(display.get())
    elif com == "MC":
        memoria = 0
    elif com == "MR":
        if memoria != 0:
            display.set("{0}".format(memoria))
            botones[memorias]["MR"].configure(bg="cyan")

def setSys(string):
    global sistema
    botones[sistemas][sistema[len(sistema)-1]].configure(bg="dark sea green")
    botones[sistemas][string].configure(bg="cyan")
    if string != "HEX":
        if string == "DEC":
            for i in range(10):
                botones[operaciones][str(i)].configure(state=NORMAL)
        if string == "OCT":
            for i in range(8):
                botones[operaciones][str(i)].configure(state=NORMAL)
            for i in ["8", "9"]:
                botones[operaciones][i].configure(state=DISABLED)
        if string == "BIN":
            for i in range(2, 10):
                botones[operaciones][str(i)].configure(state=DISABLED)
        for j in "ABCDEF":
            botones[sistemas][j].configure(state=DISABLED)
    else:
        for i in range(10):
            botones[operaciones][str(i)].configure(state=NORMAL)
        for k in "ABCDEF":
            botones[sistemas][k].configure(state=NORMAL)
    sistema.append(string)
    print(string)

def escribir(pantalla, c):
    global banderaSistTemp
    if banderaSistTemp and c in "+-*//%":
        setSys(sistema[len(sistema)-2])
    if "=" not in pantalla.get():
        pantalla.set(pantalla.get() + c)
    else:
        pantalla.set(c)

def acerca():
    filewin = Toplevel(principal)
    err = Label(filewin,fg="black",text="Calculadora\nInstituto Tecnológico de Costa Rica.\nAutor: Nicolás Feoli",font="Verdana 20")
    err.pack()

def baseTemp(pantalla, c):
    global sistemasDict
    global banderaSistTemp
    escribir(pantalla, c)
    setSys(sistemasDict[c])
    banderaSistTemp = True

def cambiarSigno(pantalla):
    disp = pantalla.get()
    if "=" in disp:
        pantalla.set(str(-int(disp[disp.index("=")+1:])))
    else:
        pantalla.set(str(-int(disp)))

#Interfaz Gráfica

principal = Tk()
principal.title("Calculadora")
principal.geometry("980x400+250+80")
principal.minsize(980,300)

#principal.resizable(width=FALSE, height=FALSE)
#principal.option_add("*Font", "Verdana 12 bold")
#fondo
Label(principal,bg="pale turquoise",width=140,height=100).place(x=-3,y=-2)
#Label(principal,bg="white",width=70,height=100).place(x=490,y=-2)

#Título
#Label(principal,bg="black",fg="white",text="Ejemplo",font="Verdana 20").place(x=200,y=50)
#Label(principal,bg="white",text="#1",font="Verdana 20").place(x=710,y=50)

#Instrucciones
#Label(principal,bg="pale turquoise",fg="black",text="Digite un número para ver si" ,font="Verdana 8").place(x=318,y=550)
#Label(principal,bg="pale turquoise",text="es positivo, negativo o 0." ,font="Verdana 8").place(x=490,y=550)

menubar = Menu(principal, bg="orchid")
filemenu = Menu(menubar, tearoff=0)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=principal.quit)
menubar.add_cascade(label="Archivo", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Manual de Usuario", command=abrirManual)
helpmenu.add_command(label="Acerca de..", command=acerca)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

principal.config(menu=menubar)

display = StringVar()
Entry(principal, font = "Verdana 12", relief=SUNKEN, textvariable=display, bg="pale turquoise", justify=CENTER).pack(side=TOP, expand=YES, fill=BOTH)

frameLeft = frame(principal, LEFT)
frameLeft.pack(fill=X, expand=False)
frameLeft.pack_propagate(5)
frameLeftSub1 = frame(frameLeft, LEFT)
frameLeftSub2 = frame(frameLeft, LEFT)
frameLeftSub1.pack(padx=5)
frameLeftSub2.pack(padx=5)
#Label(principal,bg="pale turquoise",width=140,height=100).place(x=-3,y=-2)


for key in (["DEC"], ["BIN"], ["OCT"], ["HEX"], "ABCDEF"):
    keyF = frame(frameLeftSub1, TOP, "pale turquoise")
    for char in key:
        if char in ("DEC", "BIN", "OCT", "HEX"):
            botones[sistemas][char] = crear_boton(keyF, LEFT, X, char)
        else:
            botones[sistemas][char] = crear_boton(keyF, LEFT, Y, char, lambda pantalla=display, c=char: pantalla.set(pantalla.get() + c))
            botones[sistemas][char].configure(state=DISABLED)
for char in ("DEC", "BIN", "OCT", "HEX"):
    print(char)
    botones["sys"][char].configure(command= lambda c=char: setSys(c), width=5)
    #exec("botones[\"sys\"][\"{0}\"].configure(command=setSys(\"{0}\"))".format(char2))

botones[sistemas]["DEC"].configure(bg="cyan", width=4)

for llave in (["M+"], ["M-"], ["MR"], ["MC"], ["%", "//"]):
    keyF = frame(frameLeftSub2, TOP, "pale turquoise")
    for char in llave:
        if char in ("%", "//"):
            botones[operaciones][char] = crear_boton(keyF, LEFT, BOTH, char, lambda pantalla=display, c=char: pantalla.set(pantalla.get() + c))
        else:
            botones[memorias][char] = crear_boton(keyF, LEFT, X, char, lambda c=char: operacionesMemoria(c))

for key in (("C", "+/-", "<-", "/"), "789*", "456-", "123+", ("dboh", "0", ".", "=")):
    keysF = frame(principal, TOP, "pale turquoise", 2)
    for char in key:
        if "C" in char:
            botones[operaciones][char] = crear_boton(keysF, LEFT, BOTH, char, lambda pantalla=display : pantalla.set(""))
            botones[operaciones][char].configure(width=4)
        elif "+/-" in char:
            botones[operaciones][char] = crear_boton(keysF, LEFT, BOTH, char, lambda pantalla=display : cambiarSigno(pantalla))
            botones[operaciones][char].configure(width=4)
        elif "<-" in char:
            botones[operaciones][char] = crear_boton(keysF, LEFT, BOTH, char, lambda pantalla=display : pantalla.set(pantalla.get()[:len(pantalla.get())-1]))
            botones[operaciones][char].configure(width=4)
        elif char == "=":
            botones[operaciones][char] = crear_boton(keysF, LEFT, BOTH, char, lambda pantalla=display : calcular(pantalla))
            botones[operaciones][char].configure(width=4)
            #btn.bind("<ButtonRelease-1>", lambda e, pantalla=display: calcular(pantalla), "+")
        elif char == "dboh":
            subKeysF = frame(keysF, LEFT, "pale turquoise")
            for letr in char:
                subKeysF.pack(padx=5, expand=False)
                botones[operaciones][letr] = crear_boton(subKeysF, LEFT, BOTH, letr, lambda pantalla=display, c=letr : baseTemp(pantalla, c))
                botones[operaciones][letr].configure(width=1, font = "Verdana 10", state=NORMAL)
        else:
            botones[operaciones][char] = crear_boton(keysF, LEFT, BOTH, char, lambda pantalla=display, c=char : escribir(pantalla, c))
            botones[operaciones][char].configure(width=4)


#opsF = frame(principal, LEFT)
'''
for char in "+-*/=<":
    if char == "=":
        btn = crear_boton(opsF, LEFT, BOTH, char)
        btn.bind("<ButtonRelease-1>", lambda e, pantalla=display: calcular(pantalla), "+")
    else:
        btn = crear_boton(opsF, LEFT, BOTH,char, lambda pantalla=display, s=" %s "%char: pantalla.set(pantalla.get()+s))
'''

#clearF = frame(principal, BOTTOM)
#crear_boton(clearF, LEFT, BOTH, "Clr", lambda pantalla=display: pantalla.set(""))

#entrada = StringVar()
#Entry(principal, bg="black",fg="white",font = "Verdana 12",textvariable=entrada).place(x=30,y=30)

#Boton
#Button(principal, bg="black",fg="white",font = "Verdana 12", text="Ingresar",command=lambda: valida(entrada)).place(x=620,y=295)

#Imagen
#img1 = PhotoImage(file="imagen2.gif")

#Label(principal,image=img1).place(x=20,y=400)

#Ejecuta la ventana
principal.mainloop()
