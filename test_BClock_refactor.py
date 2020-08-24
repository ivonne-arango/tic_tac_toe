 # MAIN Function
def berlinClock(time):
    HH  = int(time[0:2])
    MM  = int(time[3:5])
    HR5 = int(HH/5)
    HR1 = int(HH%5)
    MN5 = int(MM/5)
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
    SalidaF = SalidaF.replace(",","")
    SalidaF = SalidaF.replace("'","")
    SalidaF = SalidaF.replace("[","")
    SalidaF = SalidaF.replace("]","")
    SalidaF = SalidaF.replace(" " ,"")
    return str(SalidaF)

#Test for minutes all Off
def test_minutes_all_off():
        assert  berlinClock("12:00:00") == ("RROO\nRROO\nOOOOOOOOOOO")

#Test for minuts 15 minutes
def test_minutes_15():
        assert  berlinClock("08:15:00") == ("ROOO\nRRRO\nYYROOOOOOOO")

#Test for minuts 30 minutes
def test_minutes_30():
        assert  berlinClock("23:30:00") == ("RRRR\nRRRO\nYYRYYROOOOO")

#Test for minuts 45 minutes
def test_minutes_45():
        assert  berlinClock("00:45:00") == ("OOOO\nOOOO\nYYRYYRYYROO")

#Test for minuts 55 minutes
def test_minutes_55():
        assert  berlinClock("10:55:00") == ("RROO\nOOOO\nYYRYYRYYRYY")