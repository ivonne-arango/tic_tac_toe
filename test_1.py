#def validateTime(time):
#    HH = int(time[0:2])
#    MM = int(time[3:5])
#    SS = int(time[6:9])

#    if type(HH) == int and type(MM) == int and type(SS) == int:
#        if HH >= 0 and HH<=24: 
#            if MM >= 0 and MM<=59:
#                if SS >= 0 and SS<=59:
#        else:
#            print ("hora fuera de rango")
#            return "Formato inválido"

def berlinClock(time):
 #   validateTime(time)
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

#Test for midnight
#def test_midnight():
#        assert  berlinClock("00:00:00") == ("Y\nOOOO\nOOOO\nOOOOOOOOOOO\nOOOO")
#Test for valid hour with pair   seconds
def test_vh_secpair():
        assert  berlinClock("12:56:00") == ("Y\nRROO\nRROO\nYYRYYRYYRYY\nYOOO")
#Test for valid hour with inpair seconds
def test_vh_secinpair():
        assert  berlinClock("22:32:45") == ("O\nRRRR\nRROO\nYYRYYROOOOO\nYYOO")
#Test for valid hour same hour, minuts and seconds
def test_vh_010101():
        assert  berlinClock("01:01:01") == ("O\nOOOO\nROOO\nOOOOOOOOOOO\nYOOO")
#Test for valid hour one second before midnight
def test_vh_before_midnight():
        assert  berlinClock("23:59:59") == ("O\nRRRR\nRRRO\nYYRYYRYYRYY\nYYYY")

#Tests for quater of hour
#def test_nine():
#        assert  berlinClock("00:15:00") == ("Y\nOOOO\nOOOO\nYYROOOOOOOO\nOOOO")
#def test_ten():
#        assert  berlinClock("00:30:00") == ("Y\nOOOO\nOOOO\nYYRYYROOOOO\nOOOO")
#def test_eleven():
#        assert  berlinClock("00:45:00") == ("Y\nOOOO\nOOOO\nYYRYYRYYROO\nOOOO")

#Tests for hour invalid
#def test_twelve():
#        assert  berlinClock("55:23:01") == ("O\nOOOO\nOOOO\nOOOOOOOOOOO\nOOOO")

#Tests for invalid format
#def test_thirteen():
#        assert  berlinClock("ZA:00:01") == ("Formato inválido")
