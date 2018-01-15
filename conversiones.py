def aBase(num, base):
    lista_digitos = ( "0", "1", "2", "3", \
                      "4", "5", "6", "7", \
                      "8", "9", "A", "B", \
                      "C", "D", "E", "F" )
    bases = {"BIN":2,"OCT":8,"HEX":16}
    numHex = ""
    try:
        num = int(num)
        exponente = 0
        while num > 0:
            numMod = num % bases[base]
            numHex += lista_digitos[(num % bases[base])]
            num = num // bases[base]
        return(numHex)
    except ValueError as e:
        print(e)
        p = num.index(".")
        parteFlotante = num[p:]
        parteEntera = int(num[:p]) if p != 0 else ""
        exponente = 0
        numHex = a_hex(parteEntera, base) if p != 0 else "0"
        final = numHex[::-1]
        decimalesTemp = []
        decimalesHex = []
        cont = 0
        while parteFlotante not in decimalesTemp and cont < 9:
            decimalesTemp.append(parteFlotante)
            parteFlotante = str(float(parteFlotante)*bases[base])
            p = parteFlotante.index(".")
            enteroTemp = lista_digitos[int(parteFlotante[:p])]
            parteFlotante = parteFlotante[p:]
            decimalesHex.append(enteroTemp)
            cont += 1
        final += "."
        for i in decimalesHex:
            final += i
        print(final)
        return(final)

def deBase(numHex, base):
    numDec = 0
    bases = {"BIN":2,"OCT":8,"HEX":16}
    digitos = {"0":0 , "1":1 , "2":2 , "3":3 , \
               "4":4 , "5":5 , "6":6 , "7":7 , \
               "8":8 , "9":9 , "A":10, "B":11, \
               "C":12, "D":13, "E":14, "F":15  }
    if "." not in numHex:
        numHex = numHex[::-1]
        for i, j in enumerate(numHex):
            if int(j) >= bases[base]:
                return("Error, expresion mal formada.")
            if not(j.isdigit()) and j.islower():
                j = j.upper()
            numDec += digitos[j] * bases[base]**i
    else:
        flag = False
        length = len(numHex)
        p = numHex.index(".")
        print("numHex = " + str(numHex) + "; length = " + str(length) + "; -p = "  \
                          + str(-p) + "; length-p = " + str(length-p), end = "\n\n")
        for k, l in enumerate(range(-p, length-p)):
            dig = numHex[k]
            if dig != ".":
                if int(dig) >= bases[base]:
                    return("Error, expresion mal formada.")
            if  not(dig.isdigit()) and dig.islower():
                dig = j.upper()
            if numHex[k] == ".":
                print("k = " + str(k) + "; l = " + str(l) + "; dig = " + str(dig))
                flag = True
            elif not(flag):
                print("k = " + str(k) + "; l(real) = " + str(l) + "; l(usado) = " + str(l) + "; dig = " + str(dig))
                numDec += digitos[dig] * bases[base]**l
            else:
                print("k = " + str(k) + "; l(real) = " + str(l) + "; l(usado) = " + str(l-1) + "; dig = " + str(dig))
                numDec += digitos[dig] * bases[base]**(l-1)
    print("\nNumero convertido: " + str(numDec), end = "\n\n")

'''
while True:
    try:
        #aBase(input("Numero decimal a hexadecimal: "),"OCT")
        #a_octal(int(input("Numero decimal: ")))
        deBase(input("Numero base: "), "OCT")
        #de_oct(input("Numero octal: "))
    except Exception as e:
        print("Error: " + str(e))
'''
