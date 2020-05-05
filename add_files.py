from position_verify import put_position
from os import system
from files_eliminations import Eliminate

class Player:
    def __init__(self, board_file, players, names):
        self.board_file = board_file
        self.players = players
        self.names = names

    def player_add(self):
        system("cls")
        print(self.players.file_quantly()) # here print the files aviables and the board
        
        self.board_file.board_def() # here print the board
        
        print("turn of: " + self.names)
        row = input("put the row: ")
        pos_row = put_position(row, "put the row: ")
        
        column = input("put the colunm: ")
        pos_column = put_position(column, "put the colunm: ")
        
        # this is a condition for verific if the position is valid
        if self.board_file.board_ret[pos_row][pos_column] in ("·", " · "):
            if self.board_file.board_ret[pos_row][pos_column] == " · ":
                self.board_file.board_ret[pos_row][pos_column] = " "+ self.players.simbol * 1 +" "  
            else:
                self.board_file.board_ret[pos_row][pos_column] = self.players.simbol * 1
            self.players.quantl -= 1
        
        # this is an array with all possible mills
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
        
        eliminate_file = Eliminate(self.board_file, self.players) # this is the object of the class Eliminate
        
        # change1 and chage2 are arrays that contains the possible form in that a widmill can be
        change1 =[(self.players.simbol, self.players.simbol, self.players.simbol),
                  (self.players.m_simbol, self.players.simbol, self.players.simbol),
                  (self.players.simbol, self.players.m_simbol, self.players.simbol),
                  (self.players.simbol, self.players.simbol, self.players.m_simbol),
                  (self.players.m_simbol, self.players.m_simbol, self.players.simbol),
                  (self.players.simbol, self.players.m_simbol, self.players.m_simbol),
                  (self.players.m_simbol, self.players.simbol, self.players.m_simbol),]
        
        change2 =[(self.players.simbol, " " + self.players.simbol + " ", self.players.simbol),
                  (self.players.m_simbol, " " + self.players.simbol + " ", self.players.simbol),
                  (self.players.simbol, " " + self.players.m_simbol + " ", self.players.simbol),
                  (self.players.simbol, " " + self.players.simbol + " ", self.players.m_simbol),
                  (self.players.m_simbol, " " + self.players.m_simbol + " ", self.players.simbol),
                  (self.players.simbol, " " + self.players.m_simbol + " ", self.players.m_simbol),
                  (self.players.m_simbol, " " + self.players.simbol + " ", self.players.m_simbol),]
        
        # here is verify if there a widmill
        for e in range(0,len(v_e)):
            for three_simbols1 in change1:   
                # this condition verify if in the board there a widmill                                
                if three_simbols1 == (self.board_file.board_ret[v_e[e][0][0]][v_e[e][0][1]], self.board_file.board_ret[v_e[e][1][0]][v_e[e][1][1]], self.board_file.board_ret[v_e[e][2][0]][v_e[e][2][1]]):
                    self.board_file.board_ret[v_e[e][0][0]][v_e[e][0][1]] = self.players.m_simbol
                    self.board_file.board_ret[v_e[e][1][0]][v_e[e][1][1]] = self.players.m_simbol
                    self.board_file.board_ret[v_e[e][2][0]][v_e[e][2][1]] = self.players.m_simbol
                    eliminate_file.eliminate_files()
            # some positions has two space because if not the board is deformed
            # then the process is done twice
            for three_simbols2 in change2:
                if three_simbols2 == (self.board_file.board_ret[v_e[e][0][0]][v_e[e][0][1]], self.board_file.board_ret[v_e[e][1][0]][v_e[e][1][1]], self.board_file.board_ret[v_e[e][2][0]][v_e[e][2][1]]):
                    self.board_file.board_ret[v_e[e][0][0]][v_e[e][0][1]] = self.players.m_simbol
                    self.board_file.board_ret[v_e[e][1][0]][v_e[e][1][1]] = " " + self.players.m_simbol + " "
                    self.board_file.board_ret[v_e[e][2][0]][v_e[e][2][1]] = self.players.m_simbol
                    eliminate_file.eliminate_files()