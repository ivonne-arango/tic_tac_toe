def berlinClock(time):
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

def test_one():
        assert  berlinClock("00:00:00") == ("Y\nOOOO\nOOOO\nOOOOOOOOOOO\nOOOO")
def test_two():
        assert  berlinClock("12:56:00") == ("Y\nRROO\nRROO\nYYRYYRYYRYY\nYOOO")
def test_three():
        assert  berlinClock("22:32:45") == ("O\nRRRR\nRROO\nYYRYYROOOOO\nYYOO")
def test_four():
        assert  berlinClock("01:01:01") == ("O\nOOOO\nROOO\nOOOOOOOOOOO\nYOOO")
def test_five():
        assert  berlinClock("23:59:59") == ("O\nRRRR\nRRRO\nYYRYYRYYRYY\nYYYY")
def test_six():
        assert  berlinClock("00:00:01") == ("O\nOOOO\nOOOO\nOOOOOOOOOOO\nOOOO")
def test_seven():
        assert  berlinClock("04:00:00") == ("Y\nOOOO\nRRRR\nOOOOOOOOOOO\nOOOO")
def test_eight():
        assert  berlinClock("00:00:02") == ("Y\nOOOO\nOOOO\nOOOOOOOOOOO\nOOOO")


