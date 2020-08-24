 # MAIN Function
def berlinClock(time):
    HH  = int(time[0:2])
    MM  = int(time[3:5])
    HR5 = int(HH/5)
    HR1 = int(HH%5)
    MN5 = int(MM/5)
    MN1 = int(MM%5)
#Ciclo horas 5
    i=0
    salidaH1 = ["O","O","O","O"]
    while i < HR5:
        salidaH1[i]="R"      
        i += 1
    SalidaF = str(salidaH1) 
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
    return str(SalidaF)

#Test for 1 minute all Off
def test_1_minute_all_off():
        assert  berlinClock("12:00:00") == ("RROO\nRROO\nOOOOOOOOOOO\nOOOO")

#Test for 1 minute all on(Yellow).
def test_1_minute_all_on():
        assert  berlinClock("08:19:00") == ("ROOO\nRRRO\nYYROOOOOOOO\nYYYY")

#Test for 1 minut 1 minute on
def test_1_minute_1_min():
        assert  berlinClock("23:31:00") == ("RRRR\nRRRO\nYYRYYROOOOO\nYOOO")

#Test for 1 minut 2 minutes on
def test_1_minute_2_min():
        assert  berlinClock("00:47:00") == ("OOOO\nOOOO\nYYRYYRYYROO\nYYOO")

#Test for 1 minut 3 minutes on
def test_1_minute_3_min():
        assert  berlinClock("10:58:00") == ("RROO\nOOOO\nYYRYYRYYRYY\nYYYO")
