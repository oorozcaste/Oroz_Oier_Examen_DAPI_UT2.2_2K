def LeerDocumnet(nombrefichero):
    """el parametro de entrada sera el nombre de un fichero
       y a la salida tendremos una lista con los datos del 
       fichero ese"""
    file = open(nombrefichero,"r")
    lista = file.readlines()
    return(lista)

lista = LeerDocumnet("LibroCuentas.txt")
def IdentificarPagado(lista):
    """en esta funcion como parametro de entrada tendremos una lista 
       y aunque la función no devolvera nada creara un fichero en el
       que constaran todo lo pagado del fichero LibroCuentas """
    lista_pagados = open("PAGADO","w")
    for i in lista:
        if "PAGADO" in i:
            lista_pagados.write(i)
IdentificarPagado(lista)