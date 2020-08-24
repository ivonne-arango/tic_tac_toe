 # MAIN Function
def berlinClock(time):
    HH = int(time[0:2])
    HR5 = int(HH/5)
#Ciclo horas 5
    i=0
    salidaH1 = ["O","O","O","O"]
    while i < HR5:
        salidaH1[i]="R"      
        i += 1
    SalidaF = str(salidaH1) 
    SalidaF = SalidaF.replace(",","")
    SalidaF = SalidaF.replace("'","")
    SalidaF = SalidaF.replace("[","")
    SalidaF = SalidaF.replace("]","")
    SalidaF = SalidaF.replace(" " ,"")
    return str(SalidaF)


#Test for 5 hours indicator
def test_5_hours_2R2O():
        assert  berlinClock("12:00:00") == ("RROO")
def test_5_hours_4R():
        assert  berlinClock("20:00:00") == ("RRRR")
def test_5_hours_4O():
        assert  berlinClock("04:00:00") == ("OOOO")
