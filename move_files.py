from position_verify import put_position
from board import Board
from os import system
from files_eliminations import Eliminate

board_original = Board() #this variable contain the board original without changes

class Move:
    def __init__(self, board_2, player_mov, names):
        self.board_2 = board_2
        self.names = names
        self.player_mov = player_mov
        
    def fun_move(self, r_s, c_s, r_n, c_n):
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
        # in this part it is verified that when the player selects a file of one widmill, that file and all widmill
        # become the principal file
        for convert in v_e:
            if [r_s, c_s] in convert:
                if self.board_2.board_ret[convert[0][0]][convert[0][1]] == self.player_mov.m_simbol and self.board_2.board_ret[convert[1][0]][convert[1][1]] == " " + self.player_mov.m_simbol + " " and self.board_2.board_ret[convert[2][0]][convert[2][1]] == self.player_mov.m_simbol:
                    self.board_2.board_ret[convert[0][0]][convert[0][1]] = self.player_mov.simbol
                    self.board_2.board_ret[convert[1][0]][convert[1][1]] = " " + self.player_mov.simbol + " "
                    self.board_2.board_ret[convert[2][0]][convert[2][1]] = self.player_mov.simbol
                    
                if self.board_2.board_ret[convert[0][0]][convert[0][1]] == self.player_mov.m_simbol and self.board_2.board_ret[convert[1][0]][convert[1][1]] == self.player_mov.m_simbol and self.board_2.board_ret[convert[2][0]][convert[2][1]] == self.player_mov.m_simbol:
                    self.board_2.board_ret[convert[0][0]][convert[0][1]] = self.player_mov.simbol
                    self.board_2.board_ret[convert[1][0]][convert[1][1]] = self.player_mov.simbol
                    self.board_2.board_ret[convert[2][0]][convert[2][1]] = self.player_mov.simbol
                    
        # this is a condition for verific if the position is valid
        if self.board_2.board_ret[r_s][c_s] in (self.player_mov.simbol, " " + self.player_mov.simbol + " "):
                if self.board_2.board_ret[r_n][c_n] in ("·", " · "):
                    if self.board_2.board_ret[r_s][c_s] == " " + self.player_mov.simbol + " ":
                        if self.board_2.board_ret[r_n][c_n] == " · ":
                            self.board_2.board_ret[r_n][c_n] = self.board_2.board_ret[r_s][c_s]
                            self.board_2.board_ret[r_s][c_s] = board_original.board_ret[r_s][c_s]
                        else:
                            self.board_2.board_ret[r_n][c_n] = self.player_mov.simbol*1
                            self.board_2.board_ret[r_s][c_s] = board_original.board_ret[r_s][c_s]
                    else:
                        if self.board_2.board_ret[r_n][c_n] == " · ":
                            self.board_2.board_ret[r_n][c_n] = " " + self.board_2.board_ret[r_s][c_s] + " "
                            self.board_2.board_ret[r_s][c_s] = board_original.board_ret[r_s][c_s]
                        else:
                            self.board_2.board_ret[r_n][c_n] = self.player_mov.simbol*1
                            self.board_2.board_ret[r_s][c_s] = board_original.board_ret[r_s][c_s]
                    self.player_mov.turn -= 1
                    
        eliminate_file = Eliminate(self.board_2,self.player_mov) # this is the object of the class Eliminate
        
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
                if three_simbols1 == (self.board_2.board_ret[v_e[e][0][0]][v_e[e][0][1]], self.board_2.board_ret[v_e[e][1][0]][v_e[e][1][1]], self.board_2.board_ret[v_e[e][2][0]][v_e[e][2][1]]):
                    self.board_2.board_ret[v_e[e][0][0]][v_e[e][0][1]] = self.player_mov.m_simbol
                    self.board_2.board_ret[v_e[e][1][0]][v_e[e][1][1]] = self.player_mov.m_simbol
                    self.board_2.board_ret[v_e[e][2][0]][v_e[e][2][1]] = self.player_mov.m_simbol
                    eliminate_file.eliminate_files()
            # some positions has two space because if not the board is deformed
            # then the process is done twice
            for three_simbols2 in change1:   
                if three_simbols2 == (self.board_2.board_ret[v_e[e][0][0]][v_e[e][0][1]], self.board_2.board_ret[v_e[e][1][0]][v_e[e][1][1]], self.board_2.board_ret[v_e[e][2][0]][v_e[e][2][1]]):
                    self.board_2.board_ret[v_e[e][0][0]][v_e[e][0][1]] = self.player_mov.m_simbol
                    self.board_2.board_ret[v_e[e][1][0]][v_e[e][1][1]] = " " + self.player_mov.m_simbol + " "
                    self.board_2.board_ret[v_e[e][2][0]][v_e[e][2][1]] = self.player_mov.m_simbol
                    eliminate_file.eliminate_files()