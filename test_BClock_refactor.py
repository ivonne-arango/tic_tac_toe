 # MAIN Function
def berlinClock(time):
    HH  = int(time[0:2])
    MM  = int(time[3:5])
    SS = int(time[6:9])
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

#Test for seconds even number.
def test_seconds_even_number():
        assert  berlinClock("08:19:08") == ("Y\nROOO\nRRRO\nYYROOOOOOOO\nYYYY")

#est for seconds odd number.
def test_seconds_odd_number():
        assert  berlinClock("23:31:01") == ("O\nRRRR\nRRRO\nYYRYYROOOOO\nYOOO")

#Test for 59 seconds
def test_59_seconds():
        assert  berlinClock("00:47:59") == ("O\nOOOO\nOOOO\nYYRYYRYYROO\nYYOO")

#Test for 00 seconds
def test_00_seconds():
        assert  berlinClock("10:58:00") == ("Y\nRROO\nOOOO\nYYRYYRYYRYY\nYYYO")
