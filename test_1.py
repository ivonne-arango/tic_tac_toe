def validateTime(time):
    HH =time[0:2]
    MM =time[3:5]
    SS =time[6:9]
    lista1 = []

    if HH.isdigit() == False:
        lista1.append(False)
        lista1.append("Formato invalido")
        print  ("dentro del validate: ", lista1)
    else:
        lista1.append(True)
    return lista1
        
#        if HH >= 0 and HH<=24: 
#            if MM >= 0 and MM<=59:
#                if SS >= 0 and SS<=59:
#                    true
#        else:
#            print ("hora fuera de rango")
#            return "Formato inválido"

def berlinClock(time):
    validateTime(time)
    lista2 = []
    lista2 = validateTime(time)
    print (lista2)
    if lista2[0] == False:
        print ('regrese')
        print (lista2)
        return lista2
    HH = int(time[0:2])
    MM = int(time[3:5])
    SS = int(time[6:9])
    HR5 = int(HH/5)
    HR1 = int(HH%5)
    MN5 = int(MM/5)
    MN1 = int(MM%5)
    SD1 = int(SS%2)
    SD = "O"
    SalidaF =""
    if (SD1 == 0):
        SD = "Y"
    print ("HH: " ,HH)    
    print ("MM: ", MM)    
    print ("SS: ", SS)    
    print ("HR5: ", HR5)    
    print ("HR1: ", HR1)    
    print ("MN5: ", MN5)    
    print ("MN1: ", MN1)    
    print ("SD1: ",SD1)    
    print ("SD: ",SD)    

#Ciclo horas 5
    i=0
    salidaH1 = ["O","O","O","O"]
    while i < HR5:
        print (i) 
        salidaH1[i]="R"      
        i += 1
    SalidaF = SalidaF + "\n" + str(salidaH1)  
#Ciclo por horas 1
    salidaH2 = ["O","O","O","O"]
    i=0
    while i < HR1:
        salidaH2[i]="R"
        i += 1  
    SalidaF = SalidaF + "\n" + str(salidaH2)
#Ciclo por minutos 5
    salidaM1 = ["O","O","O","O","O","O","O","O","O","O","O"]
    i=0
    while i< MN5:
        if (i == 2 or i==5 or i==8):
            salidaM1[i]="R"
        else: 
            salidaM1[i]="Y"
        i += 1  
    SalidaF = SalidaF + "\n" + str(salidaM1) 
#Ciclo por minuto
    salidaM2 = ["O","O","O","O"]
    i = 0
    while i < MN1:
        salidaM2[i]="Y"
        i += 1
    SalidaF = SalidaF + "\n" + str(salidaM2)
    SalidaF = SalidaF.replace(",","")
    SalidaF = SalidaF.replace("'","")
    SalidaF = SalidaF.replace("[","")
    SalidaF = SalidaF.replace("]","")
    SalidaF = SalidaF.replace(" " ,"")
    print  (str(SD + SalidaF))
    return str(SD + SalidaF) 

#Tests for invalid format
def test_invalid_format():
        assert  berlinClock("XX:00:01") == [False,'Formato invalido']                                        
