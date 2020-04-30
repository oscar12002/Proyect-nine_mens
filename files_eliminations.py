from board import Board
from os import system
from position_verify import put_position

class Eliminate:
    def __init__(self, board_e, file_eliminate):
        self.board_e = board_e
        self.file_eliminate = file_eliminate
        
    def eliminate_files(self):
        system("cls")
        self.board_e.board_def()
        
        eliminate_turn = 0
        while eliminate_turn != 1:
            row = input("row that you want eliminate: ")
            row_eliminate = put_position(row, "row that you want eliminate: ")
            
            column = input("column that you want eliminate: ")
            column_eliminate = put_position(column, "column that you want eliminate: ")
            
            if self.file_eliminate.simbol == "●":
                if self.board_e.board_ret[row_eliminate][column_eliminate] == "○":
                    self.board_e.board_ret[row_eliminate][column_eliminate] = "·"
                    eliminate_turn += 1
                    
                if self.board_e.board_ret[row_eliminate][column_eliminate] == " ○ ":
                    self.board_e.board_ret[row_eliminate][column_eliminate] = " · "
                    eliminate_turn += 1
                    
            if self.file_eliminate.simbol == "○":
                if self.board_e.board_ret[row_eliminate][column_eliminate] == "●":
                    self.board_e.board_ret[row_eliminate][column_eliminate] = "·"
                    eliminate_turn += 1
                    
                if self.board_e.board_ret[row_eliminate][column_eliminate] == " ● ":
                    self.board_e.board_ret[row_eliminate][column_eliminate] = " · "
                    eliminate_turn += 1
                    