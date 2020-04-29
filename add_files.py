from position_verify import put_position
from os import system
from files_eliminations import Eliminate


class Player:
    def __init__(self,board_file,players,names):
        self.board_file = board_file
        self.players = players
        self.names = names
        
                
    def player_add(self):
        system("cls")
        # here print the files aviables and the board
        print(self.players.file_quantly())
        # print(file_player_two.file_quantly())
        
        self.board_file.board_def()
        
        print("turn of: " + self.names)
        row = input("put the row: ")
        pos_row = put_position(row,"put the row: ")
        
        column = input("put the colunm: ")
        pos_column = put_position(column,"put the colunm: ")
        
        # this is a condition for verific if the position is valid
        if self.board_file.board_ret[pos_row][pos_column] in ("·", " · "):
            if self.board_file.board_ret[pos_row][pos_column] == " · ":
                self.board_file.board_ret[pos_row][pos_column] = " "+ self.players.simbol * 1 +" "  
            else:
                self.board_file.board_ret[pos_row][pos_column] = self.players.simbol * 1
            self.players.quantl -= 1
        eliminate_file = Eliminate(self.board_file,self.players)
        if self.board_file.elimin(self.players,self.board_file.board_ret):
            eliminate_file.eliminate_files()
        