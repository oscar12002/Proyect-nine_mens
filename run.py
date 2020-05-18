from add_files import Player
from board import Board
from files import File
from position_verify import put_position
from os import system
from move_verify import verify_move
from tqdm import tqdm
from move_files import Move

# here are created the objects
system("cls")
name_of_player_one = input("PLAYER ONE ➡️  your files are white"+"\n"+
                "enter your name: ")
name_of_player_two = input("PLAYER TWO ➡️  your files are black"+"\n"+
                "enter your name: ")

board_player = Board()
file_one = File("●","◍")
file_two = File("○","◌")
player_one_add = Player(board_player, file_one, name_of_player_one)
player_two_add = Player(board_player, file_two, name_of_player_two)

player_move_one = Move(board_player, file_one, name_of_player_one)
player_move_two = Move(board_player, file_two, name_of_player_two)

# in this function the momevents are ejecuted with the verification
quantl_files_1 = 0
quantl_files_2 = 0
def movements(board_2, names):
            # this variables are for control the quantity of the files. if the player has three files
            global quantl_files_1, quantl_files_2
            
            system("cls")
            board_2.board_def()
            
            print("turn of: {}".format(names))
            
            select_row = input("select the row: ")
            pos_select_row = put_position(select_row,"select the row: ")
            
            select_column = input("select the column: ")
            pos_select_column = put_position(select_column,"select the colunm: ")
            
            move_to_row = input("move to row: ")
            pos_move_to_row = put_position(move_to_row,"move to row: ")

            move_to_column = input("move to column: ")
            pos_move_to_column = put_position(move_to_column,"move to colunm: ")
            
            # this for count the number of files for every player in the board
            for e in range(len(board_2.board_ret)):
                for fil in board_2.board_ret[e]:
                    if fil == file_one.simbol or fil == file_one.m_simbol or fil == " " + file_one.simbol + " " or fil == " " + file_one.m_simbol + " ":
                        quantl_files_1 += 1
                    if fil == file_two.simbol or fil == file_two.m_simbol or fil == " " + file_two.simbol + " " or fil == " " + file_two.m_simbol + " ":
                        quantl_files_2 += 1
            # here is verified if the playes has three files or more
            if quantl_files_1 == 3 or quantl_files_2 == 3:
                if file_one.turn+1 > file_two.turn:
                    # this other condition is for control the turn of the player
                    if quantl_files_1 == 3:
                        player_move_one.fun_move(pos_select_row, pos_select_column, pos_move_to_row, pos_move_to_column)
                    else:    
                        verify_move(pos_select_row, pos_select_column, pos_move_to_row, pos_move_to_column, file_one, file_two, player_move_one, player_move_two)

                if file_two.turn > file_one.turn:
                    if quantl_files_2 == 3:
                        player_move_two.fun_move(pos_select_row, pos_select_column, pos_move_to_row, pos_move_to_column)
                    else:
                        verify_move(pos_select_row, pos_select_column, pos_move_to_row, pos_move_to_column, file_one, file_two, player_move_one, player_move_two)                        

            else:  
                # else is called the function move with the verification
                verify_move(pos_select_row, pos_select_column, pos_move_to_row, pos_move_to_column, file_one, file_two, player_move_one, player_move_two)  
            
def main():
    global quantl_files_1, quantl_files_2
    # this part is for a loading bar
    system("cls")
    loob = tqdm(total= 5000, position= 0, leave= False)
    for k in range(5000):
        loob.set_description("Loading game...".format(k))
        loob.update(1)
    loob.close()
    
    # here the turn of the players is controlled
    while (file_one.quantl + file_two.quantl) > 0:
        while file_one.quantl+1 > file_two.quantl:
            player_one_add.player_add()

        while file_two.quantl > file_one.quantl:
            player_two_add.player_add()
    
    # this part is for the movement
    while True:
        # also controls the turn
        while file_one.turn+1 > file_two.turn:
            # is called the function movement
            movements(board_player,player_move_one.names)
            print(quantl_files_1)
            # this part is for verified if the player has two files. if has two files that player lose
            if quantl_files_1 == 2:
                system("cls")
                print("player '{}' haven't enough files. player '{}' WIN!!!!".format(player_move_one.names, player_move_two.names))
                return False
            if quantl_files_2 == 2:
                system("cls")
                print("player '{}' haven't enough files. player '{}' WIN!!!!".format(player_move_two.names, player_move_one.names))
                return False
            quantl_files_1 = 0
            quantl_files_2 = 0
        while file_two.turn > file_one.turn:
            movements(board_player,player_move_two.names)
            if quantl_files_1 == 2:
                system("cls")
                print("player '{}' haven't enough files. player '{}' WIN!!!!".format(player_move_one.names, player_move_two.names))
                return False
            if quantl_files_2 == 2:
                system("cls")
                print("player '{}' haven't enough files. player '{}' WIN!!!!".format(player_move_two.names, player_move_one.names))
                return False
            quantl_files_1 = 0
            quantl_files_2 = 0
            
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n salida forzosa")