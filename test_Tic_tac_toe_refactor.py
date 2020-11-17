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

def validation_seconds_first_line(SegundosBerlin):
    SalidaSegundos = "O"  
    if (SegundosBerlin == 0):
        SalidaSegundos = "Y" 
    return SalidaSegundos

def loop5hours_second_line(HorasBerlin5):
    i=0
    SalidaHoras5 = ["O","O","O","O"]
    while i < HorasBerlin5:
        SalidaHoras5[i]="R"      
        i += 1
    return ("\n" + str(SalidaHoras5))
#
#
def loop1hour_third_line(HorasBerlin1):
    SalidaHoras1 = ["O","O","O","O"]
    i=0
    while i < HorasBerlin1:
        SalidaHoras1[i]="R"
        i += 1  
    return ("\n" + str(SalidaHoras1))
#
#
def loop5minutes_fourth_line(MinutosBerlin5):
    SalidaMinutos5 = ["O","O","O","O","O","O","O","O","O","O","O"]
    i=0
    while i< MinutosBerlin5:
        if (i == 2 or i==5 or i==8):
            SalidaMinutos5[i]="R"
        else: 
            SalidaMinutos5[i]="Y"
        i += 1  
    return("\n" + str(SalidaMinutos5))
#
# 
def loop1minute_fifth_line(MinutosBerlin1):
    SalidaMinutos1 = ["O","O","O","O"]
    i = 0
    while i < MinutosBerlin1:
        SalidaMinutos1[i]="Y"
        i += 1
    return("\n" + str(SalidaMinutos1))
#
#   
# MAIN Function
def berlinClock(time):
#   validateTime(time)
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
#    
    SalidaBerlin = SalidaBerlin + validation_seconds_first_line(SegundosBerlin)
#
    SalidaBerlin = SalidaBerlin + loop5hours_second_line(HorasBerlin5)
    SalidaBerlin = SalidaBerlin + loop1hour_third_line(HorasBerlin1)
    SalidaBerlin = SalidaBerlin + loop5minutes_fourth_line(MinutosBerlin5)
    SalidaBerlin = SalidaBerlin + loop1minute_fifth_line(MinutosBerlin1)

    SalidaBerlin = SalidaBerlin.replace(",","")
    SalidaBerlin = SalidaBerlin.replace("'","")
    SalidaBerlin = SalidaBerlin.replace("[","")
    SalidaBerlin = SalidaBerlin.replace("]","")
    SalidaBerlin = SalidaBerlin.replace(" " ,"")
    return SalidaBerlin
#
#
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