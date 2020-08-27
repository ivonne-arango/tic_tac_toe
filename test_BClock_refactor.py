def validateTime(time):
    HoraValidate     = time[0:2]
    MinutosValidate  = time[3:5]
    SegundosValidate = time[6:9]
    SalidaValidate   = []
#Validate format
    if HoraValidate.isdigit() == False or MinutosValidate.isdigit() == False or SegundosValidate.isdigit() == False: 
        SalidaValidate.append(False)
        SalidaValidate.append("Formato invalido")
        return SalidaValidate 
#Validate range for hours, minutes and seconds
    if (int(HoraValidate) >= 0 and int(HoraValidate)<=23) and (int(MinutosValidate) >= 0 and int(MinutosValidate)<=59) and (int(SegundosValidate) >= 0 and int(SegundosValidate)<=59):
        SalidaValidate.append(True)
    else:
        SalidaValidate.append(False)
        SalidaValidate.append("Hora fuera de rango")   
    return SalidaValidate    

 # MAIN Function
def berlinClock(time):
    validateTime(time)
    SalidaBerlinErr   = []
    SalidaBerlinErr   = validateTime(time)
    if SalidaBerlinErr[0] == False:
        return SalidaBerlinErr
#Variables Definition
    HorasBerlin     = int(time[0:2])
    MinutosBerlin   = int(time[3:5])
    SegungosBerlin  = int(time[6:9])
    HorasBerlin5    = int(HorasBerlin/5)
    HorasBerlin1    = int(HorasBerlin%5)
    MinutosBerlin5  = int(MinutosBerlin/5)
    MinutosBerlin1  = int(MinutosBerlin%5)
    SegundosBerlin  = int(SegungosBerlin%2)
    SalidaBerlin =""
#Loop per 5 hours,variable i, is a counter
    i=0
    SalidaHoras5 = ["O","O","O","O"]
    while i < HorasBerlin5:
        SalidaHoras5[i]="R"      
        i += 1
    SalidaBerlin = "\n" + str(SalidaHoras5)
#Loop per 1 hour, variable i, is a counter
    SalidaHoras1 = ["O","O","O","O"]
    i=0
    while i < HorasBerlin1:
        SalidaHoras1[i]="R"
        i += 1  
    SalidaBerlin = SalidaBerlin + "\n" + str(SalidaHoras1)
#Loop per 5 minutes, variable i, is a counter
    SalidaMinutos5 = ["O","O","O","O","O","O","O","O","O","O","O"]
    i=0
    while i< MinutosBerlin5:
        if (i == 2 or i==5 or i==8):
            SalidaMinutos5[i]="R"
        else: 
            SalidaMinutos5[i]="Y"
        i += 1  
    SalidaBerlin = SalidaBerlin + "\n" + str(SalidaMinutos5) 
#Loop per 1 minute, variable i, is a counter
    SalidaMinutos1 = ["O","O","O","O"]
    i = 0
    while i < MinutosBerlin1:
        SalidaMinutos1[i]="Y"
        i += 1
    SalidaBerlin = SalidaBerlin + "\n" + str(SalidaMinutos1)
#Loop per seconds
    SalidaSegundos = "O"  
    if (SegundosBerlin == 0):
        SalidaSegundos = "Y" 

    SalidaBerlin = SalidaBerlin.replace(",","")
    SalidaBerlin = SalidaBerlin.replace("'","")
    SalidaBerlin = SalidaBerlin.replace("[","")
    SalidaBerlin = SalidaBerlin.replace("]","")
    SalidaBerlin = SalidaBerlin.replace(" " ,"")
    return str(SalidaSegundos + SalidaBerlin) 


#Test for correct hour esc1.
def test_correct_hour_esc1():
        assert  berlinClock("08:19:08") == ("Y\nROOO\nRRRO\nYYROOOOOOOO\nYYYY")
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