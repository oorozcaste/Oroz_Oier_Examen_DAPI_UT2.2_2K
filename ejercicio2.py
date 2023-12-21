hiztegia = {}

while True:
    korrikalari = input("intoduce la hora y el punto kilometriko separados por un espacio: ")
    bukaera = input("ha terminado la carrera(si/no)")
    
    if bukaera != "si":
        datuak = korrikalari.split(" ")
        hiztegia[datuak[0]] = datuak[1]
        
    else:
        datuak = korrikalari.split(" ")
        hiztegia[datuak[0]] = datuak[1]
        
        x = hiztegia.keys()
        y = hiztegia.values()
        x = list(x)
        y = list(y)
        for i in range(len(x)):
            print(f"El corredor a las {x[i]} estaba en el kilometro {y[i]}")
       
        break
    
        

        
    
    
