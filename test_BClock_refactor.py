def validateTime(time):
    HH =time[0:2]
    MM =time[3:5]
    SS =time[6:9]
    lista1 = []
#Validate format
    if HH.isdigit() == False or MM.isdigit() == False or SS.isdigit() == False: 
        lista1.append(False)
        lista1.append("Formato invalido")
        return lista1
#Validate range for hours, minutes and seconds
    if (int(HH) >= 0 and int(HH)<=23) and (int(MM) >= 0 and int(MM)<=59) and (int(SS) >= 0 and int(SS)<=59):
        lista1.append(True)
    else:
        lista1.append(False)
        lista1.append("Hora fuera de rango")
    
    return lista1
 # MAIN Function
def berlinClock(time):
    validateTime(time)
    lista2 = []
    lista2 = validateTime(time)
    if lista2[0] == False:
        return lista2
    HH  = int(time[0:2])
    MM  = int(time[3:5])
    SS  = int(time[6:9])
    HR5 = int(HH/5)
    HR1 = int(HH%5)
    MN5 = int(MM/5)
    MN1 = int(MM%5)
    SD1 = int(SS%2)
    SalidaF =""
#Ciclo horas 5
    i=0
    salidaH1 = ["O","O","O","O"]
    while i < HR5:
        salidaH1[i]="R"      
        i += 1
    SalidaF = "\n" + str(salidaH1)
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
    #Ciclo per seconds
    SD = "O"  
    if (SD1 == 0):
        SD = "Y" 

    SalidaF = SalidaF.replace(",","")
    SalidaF = SalidaF.replace("'","")
    SalidaF = SalidaF.replace("[","")
    SalidaF = SalidaF.replace("]","")
    SalidaF = SalidaF.replace(" " ,"")
    return str(SD + SalidaF) 

#Test for invalid format hour.
def test_invalid_format_hour():
        assert  berlinClock("AA:19:08") == [False,'Formato invalido']
#Test for invalid range hour.
def test_invalid_range_hour():
        assert  berlinClock("24:00:00") == [False,'Hora fuera de rango']
#Test for invalid format minutes.
def test_invalid_format_minutes():
        assert  berlinClock("08:MM:08") == [False,'Formato invalido']
#Test for invalid range minutes.
def test_invalid_range_minutes():
        assert  berlinClock("08:60:08") == [False,'Hora fuera de rango']
#Test for invalid format seconds.
def test_invalid_format_seconds():
        assert  berlinClock("08:19:SS") == [False,'Formato invalido']
#Test for invalid range seconds.
def test_invalid_range_seconds():
        assert  berlinClock("08:19:90") == [False,'Hora fuera de rango']
#Test for correct hour esc1.
def test_correct_hour_esc1():
        assert  berlinClock("08:19:08") == ("Y\nROOO\nRRRO\nYYROOOOOOOO\nYYYY")
#Test for correct hour esc2.
def test_correct_hour_esc2():
        assert  berlinClock("23:31:01") == ("O\nRRRR\nRRRO\nYYRYYROOOOO\nYOOO")
#Test for correct hour esc3
def test_correct_hour_esc3():
        assert  berlinClock("00:47:59") == ("O\nOOOO\nOOOO\nYYRYYRYYROO\nYYOO")
