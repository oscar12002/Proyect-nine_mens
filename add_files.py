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
        
        v_e =[[[0,0],[0,3],[0,6]],
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
            [[1,5],[3,4],[5,5]],
            [[0,6],[3,6],[6,6]]]
        
        eliminate_file = Eliminate(self.board_file,self.players)
        for e in range(0,len(v_e)):
            if (self.players.simbol,self.players.simbol,self.players.simbol) == (self.board_file.board_ret[v_e[e][0][0]][v_e[e][0][1]],self.board_file.board_ret[v_e[e][1][0]][v_e[e][1][1]],self.board_file.board_ret[v_e[e][2][0]][v_e[e][2][1]]):
                self.board_file.board_ret[v_e[e][0][0]][v_e[e][0][1]] = self.players.m_simbol
                self.board_file.board_ret[v_e[e][1][0]][v_e[e][1][1]] = self.players.m_simbol
                self.board_file.board_ret[v_e[e][2][0]][v_e[e][2][1]] = self.players.m_simbol
                eliminate_file.eliminate_files()
            if (self.players.simbol," " + self.players.simbol + " ",self.players.simbol) == (self.board_file.board_ret[v_e[e][0][0]][v_e[e][0][1]],self.board_file.board_ret[v_e[e][1][0]][v_e[e][1][1]],self.board_file.board_ret[v_e[e][2][0]][v_e[e][2][1]]):
                self.board_file.board_ret[v_e[e][0][0]][v_e[e][0][1]] = self.players.m_simbol
                self.board_file.board_ret[v_e[e][1][0]][v_e[e][1][1]] = " " + self.players.m_simbol + " "
                self.board_file.board_ret[v_e[e][2][0]][v_e[e][2][1]] = self.players.m_simbol
                eliminate_file.eliminate_files()
