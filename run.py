from add_files import Player
from board import Board
from files import File
from position_verify import put_position
from os import system

from move_files import Move

system("cls")
name_of_player_one = input("PLAYER ONE ➡️  your files are white"+"\n"+
                   "enter your name: ")
name_of_player_two = input("PLAYER TWO ➡️  your files are black"+"\n"+
                   "enter your name: ")


board_player = Board()
file_one = File("●")
file_two = File("○")
player_one_add = Player(board_player, file_one, name_of_player_one)
player_two_add = Player(board_player, file_two, name_of_player_two)

player_move_one = Move(board_player, file_one, name_of_player_one)
player_move_two = Move(board_player, file_two, name_of_player_two)

def movements(board_2,names):
        system("cls")
        board_2.board_def()
        
        print("turn of: " + names)
        select_row = input("select the row: ")
        pos_select_row = put_position(select_row,"select the row: ")
        
        
        select_column = input("select the column: ")
        pos_select_column = put_position(select_column,"select the colunm: ")
        
        
        move_to_row = input("move to row: ")
        pos_move_to_row = put_position(move_to_row,"move to row: ")
        
        
        move_to_column = input("move to column: ")
        pos_move_to_column = put_position(move_to_column,"move to colunm: ")
       
        if (pos_select_row+1, pos_select_column+1) in ((1,1), (1,4), (1,7), (4,1), (7,1), (7,4), (7,7), (4,7)):
            if (pos_move_to_row+1, pos_move_to_column+1) in ((pos_select_row+1, pos_select_column+4), (pos_select_row+1, pos_select_column-2), (pos_select_row+4, pos_select_column+1), (pos_select_row-2, pos_select_column+1)):
                if file_one.turn+1 > file_two.turn:
                    player_move_one.fun_move(pos_select_row,pos_select_column,pos_move_to_row,pos_move_to_column)

                if file_two.turn > file_one.turn:
                    player_move_two.fun_move(pos_select_row,pos_select_column,pos_move_to_row,pos_move_to_column)
        
        if (pos_select_row+1, pos_select_column+1) in ((2,2), (2,4), (2,6), (4,2), (6,2), (6,4), (6,6), (4,6)):
            if (pos_move_to_row+1, pos_move_to_column+1) in ((pos_select_row+1, pos_select_column+3), (pos_select_row+1, pos_select_column-1), (pos_select_row+3, pos_select_column+1), (pos_select_row-1, pos_select_column+1)):
                if file_one.turn+1 > file_two.turn:
                    player_move_one.fun_move(pos_select_row,pos_select_column,pos_move_to_row,pos_move_to_column)

                if file_two.turn > file_one.turn:
                    player_move_two.fun_move(pos_select_row,pos_select_column,pos_move_to_row,pos_move_to_column)
            
        if (pos_select_row+1, pos_select_column+1) in ((4,1), (4,2), (4,6), (4,7)):
            if (pos_move_to_row+1, pos_move_to_column+1) in ((pos_select_row+1, pos_select_column+2), (pos_select_row+1, pos_select_column)):  
                if file_one.turn+1 > file_one.turn:
                    player_move_one.fun_move(pos_select_row,pos_select_column,pos_move_to_row,pos_move_to_column)

                if file_two.turn > file_one.turn:
                    player_move_two.fun_move(pos_select_row,pos_select_column,pos_move_to_row,pos_move_to_column)
                        
        if (pos_select_row+1, pos_select_column+1) in ((1,4), (2,4), (6,4), (7,4)):
            if (pos_move_to_row+1, pos_move_to_column+1) in ((pos_select_row+2, pos_select_column+1), (pos_select_row, pos_select_column+1)):  
                if file_one.turn+1 > file_two.turn:
                    player_move_one.fun_move(pos_select_row,pos_select_column,pos_move_to_row,pos_move_to_column)

                if file_two.turn > file_one.turn:
                    player_move_two.fun_move(pos_select_row,pos_select_column,pos_move_to_row,pos_move_to_column)
                        
        
        if (pos_select_row+1, pos_select_column+1) in ((3,3), (3,4), (3,5), (4,3), (5,3), (5,4), (5,5), (4,5)):
            if (pos_move_to_row+1, pos_move_to_column+1) in ((pos_select_row+1, pos_select_column+2), (pos_select_row+1, pos_select_column), (pos_select_row+2, pos_select_column+1), (pos_select_row, pos_select_column+1)):
                if file_one.turn+1 > file_two.turn:
                    player_move_one.fun_move(pos_select_row,pos_select_column,pos_move_to_row,pos_move_to_column)

                if file_two.turn > file_one.turn:
                    player_move_two.fun_move(pos_select_row,pos_select_column,pos_move_to_row,pos_move_to_column)

def main():
    while (file_one.quantl + file_two.quantl) > 0:
        while file_one.quantl+1 > file_two.quantl:
            player_one_add.player_add()

        while file_two.quantl > file_one.quantl:
            player_two_add.player_add() 
            
    while True:
        while file_one.turn+1 > file_two.turn:
            movements(board_player,player_move_one.names)

        while file_two.turn > file_one.turn:
            movements(board_player,player_move_two.names)
            
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n salida forzosa")
