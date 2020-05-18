from board import Board
from os import system
from position_verify import put_position

class Eliminate: # With this class the files are eliminated
    def __init__(self, board_e, file_eliminate):
        self.board_e = board_e
        self.file_eliminate = file_eliminate

    def activate(self, row, column):
        v_e =  [[[0,0],[0,3],[0,6]],
                [[1,1],[1,3],[1,5]],
                [[2,2],[2,3],[2,4]],
                [[3,0],[3,1],[3,2]],
                [[3,4],[3,5],[3,6]],
                [[4,2],[4,3],[4,4]],
                [[5,1],[4,3],[5,5]],
                [[6,0],[6,3],[6,6]],
                
                [[1,1],[3,1],[5,1]],
                [[0,0],[3,0],[6,0]],
                [[2,2],[3,2],[4,2]],
                [[0,3],[1,3],[2,3]],
                [[4,3],[5,3],[6,3]],
                [[2,4],[3,4],[4,4]],
                [[1,5],[3,5],[5,5]],
                [[0,6],[3,6],[6,6]]]
    
        for convert in v_e:
            if [row, column] in convert:
                if self.board_e.board_ret[convert[0][0]][convert[0][1]] in ("◌","◍") and self.board_e.board_ret[convert[1][0]][convert[1][1]] in ("◌","◍") and self.board_e.board_ret[convert[2][0]][convert[2][1]] in ("◌","◍"):
                    return True
                
    def eliminate_files(self):
        system("cls")
        self.board_e.board_def()
        
        eliminate_turn = 0 # this variable is for control the turns
        while eliminate_turn != 1:
            row = input("row that you want eliminate: ")
            row_eliminate = put_position(row, "row that you want eliminate: ")
            
            column = input("column that you want eliminate: ")
            column_eliminate = put_position(column, "column that you want eliminate: ")
            
            # In this conditions it does the process of eliminate
            if self.file_eliminate.simbol == "●":
                if self.board_e.board_ret[row_eliminate][column_eliminate] == "○":
                    self.board_e.board_ret[row_eliminate][column_eliminate] = "·"
                    eliminate_turn += 1
                # some positions has two space because if not the board is deformed
                # then the process is done twice
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
                    
            # if the file selected is in a widmill the player can´t eliminate
            if self.activate(row_eliminate, column_eliminate) != True:  
                if self.file_eliminate.simbol == "●":
                    if self.board_e.board_ret[row_eliminate][column_eliminate] == "◌":
                        self.board_e.board_ret[row_eliminate][column_eliminate] = "·"
                        eliminate_turn += 1
                    # some positions has two space because if not the board is deformed
                    # then the process is done twice
                    if self.board_e.board_ret[row_eliminate][column_eliminate] == " ◌ ":
                        self.board_e.board_ret[row_eliminate][column_eliminate] = " · "
                        eliminate_turn += 1
                        
                if self.file_eliminate.simbol == "○":
                    if self.board_e.board_ret[row_eliminate][column_eliminate] == "◍":
                        self.board_e.board_ret[row_eliminate][column_eliminate] = "·"
                        eliminate_turn += 1
                        
                    if self.board_e.board_ret[row_eliminate][column_eliminate] == " ◍ ":
                        self.board_e.board_ret[row_eliminate][column_eliminate] = " · "
                        eliminate_turn += 1
                                    