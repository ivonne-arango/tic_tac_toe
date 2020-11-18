#import random
#def bots():


 # MAIN Function
def Tic_tac_toe(data_array):
    i=0
    ganador = ""
    while i< 9:
        if data_array[2] == "X" and  data_array[5] == "X" and data_array[8] == "X":
            ganador = "X"
        if data_array[0] == "X" and  data_array[1] == "X" and data_array[2] == "X":
            ganador = "X"
        if data_array[3] == "X" and  data_array[4] == "X" and data_array[5] == "X":
            ganador = "X"
        if data_array[6] == "X" and  data_array[7] == "X" and data_array[8] == "X":
            ganador = "X"
        if data_array[0] == "X" and  data_array[3] == "X" and data_array[6] == "X":
            ganador = "X"
        if data_array[0] == "X" and  data_array[4] == "X" and data_array[8] == "X":
            ganador = "X"
        if data_array[1] == "X" and  data_array[4] == "X" and data_array[7] == "X":
            ganador = "X"
        if data_array[0] == "O" and  data_array[1] == "O" and data_array[2] == "O":
            ganador = "O"
        if data_array[3] == "O" and  data_array[4] == "O" and data_array[5] == "O":
            ganador = "O"
        if data_array[6] == "O" and  data_array[7] == "O" and data_array[8] == "O":
            ganador = "O"
        if data_array[0] == "O" and  data_array[3] == "O" and data_array[6] == "O":
            ganador = "O"
        if data_array[0] == "O" and  data_array[4] == "O" and data_array[8] == "O":
            ganador = "O"
        if data_array[1] == "O" and  data_array[4] == "O" and data_array[7] == "O":
            ganador = "O"
        if data_array[2] == "O" and  data_array[5] == "O" and data_array[8] == "O":
            ganador = "O"
        i+=1
    if ganador == '':
        salida = "empate"
    else:
        salida = "Ganador: " + ganador
    return salida

#Tests for invalid hour
def test_gana_X_horizontal():
        assert  Tic_tac_toe(["X","X","X","O","O","","X","0","X"]) == 'Ganador: X'   
def test_gana_X_vertical():
        assert  Tic_tac_toe(["O","X","O","O","X","X","","X","O"]) == 'Ganador: X'  
def test_gana_O_vertical_con_vacios():
        assert  Tic_tac_toe(["O","","X","","","X","","X","X"]) == 'Ganador: X'  
def test_gana_X_diagonal():
        assert  Tic_tac_toe(["X","O","X","X","X","","O","0","X"]) == 'Ganador: X'
def test_gana_X_horizontal_con_vacios():
        assert  Tic_tac_toe(["","","","X","X","X","","",""]) == 'Ganador: X' 
def test_gana_O_horizontal():
        assert  Tic_tac_toe(["O","O","O","X"," ","X","","",""]) == 'Ganador: O' 
def test_gana_O_vertical():
        assert  Tic_tac_toe(["X","","O","","","O","X","X","O"]) == 'Ganador: O' 
def test_gana_O_diagonal():
        assert  Tic_tac_toe(["O","","","X","O","","X","X","O"]) == 'Ganador: O' 
def test_gana_O_diagonal():
        assert  Tic_tac_toe(["O","X","O","X","X","O","X","O","X"]) == 'empate' 



