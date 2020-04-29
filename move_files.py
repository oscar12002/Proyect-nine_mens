from position_verify import put_position
from board import Board
from os import system
from files_eliminations import Eliminate


board_original = Board()

class Move:
    def __init__(self,board_2,player_mov,names):
        self.board_2 = board_2
        self.names = names
        self.player_mov = player_mov
        
    def fun_move(self,r_s,c_s,r_n,c_n):
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
        eliminate_file = Eliminate(self.board_2,self.player_mov)
        if self.board_2.elimin(self.player_mov,self.board_2.board_ret):
            eliminate_file.eliminate_files()
