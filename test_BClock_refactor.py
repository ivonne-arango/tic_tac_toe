 # MAIN Function
def berlinClock(time):
    HH = int(time[0:2])
    HR5 = int(HH/5)
    HR1 = int(HH%5)
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
    SalidaF = SalidaF.replace(",","")
    SalidaF = SalidaF.replace("'","")
    SalidaF = SalidaF.replace("[","")
    SalidaF = SalidaF.replace("]","")
    SalidaF = SalidaF.replace(" " ,"")
    return str(SalidaF)

#Test for 1 hour indicator
def test_1_hour_2R2O():
        assert  berlinClock("12:00:00") == ("RROO\nRROO")
def test_1_hour_4R():
        assert  berlinClock("19:00:00") == ("RRRO\nRRRR")
def test_1_hour_4O():
        assert  berlinClock("05:00:00") == ("ROOO\nOOOO")
