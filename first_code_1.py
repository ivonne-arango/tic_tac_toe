#import random
#def bots():


 # MAIN Function
def Tic_tac_toe(data_array):
    i=0
    ganador = ""
    while i< 9:
        if data_array[0] == "X" and  data_array[1] == "X" and data_array[2] == "X":
            ganador = "X"
            print ('x')
        if data_array[0] == "O" and data_array[1] == "O" and data_array[2] == "O":
            ganador = 'O'
        i+=1
        print ('while')
    if ganador == '':
        print ('emp')
        salida = "empate"
    else:
        salida = "Ganador: " + ganador
    return salida

#Tests for invalid hour
def test_gana_X_horizontal():
        assert  Tic_tac_toe(["X","X","X","O","O","","X","0","X"]) == 'Ganador: X'   
def test_gana_X_vertical():
        assert  Tic_tac_toe("O,X,O,O,X,X,O,X,O") == ['Ganador: X']  
def test_gana_X_diagonal():
        assert  Tic_tac_toe("X,O,X,X,X, ,O,O,X") == ['Ganador: X']                                    

