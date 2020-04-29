# from add import file_player_one, file_player_two
class Board:
    def __init__(self):
        self.a = ["·","——","——","·","——","——","·"]
        self.b = ["| ","·","——","·","——","·"," |"]
        self.c = ["| ","| ","·","·","·"," |"," |"]
        self.d = ["·"," · ","·"," ","·"," · ","·"]
        self.e = ["| ","| ","·","·","·"," |"," |"]
        self.f = ["| ","·","——","·","——","·"," |"]
        self.g = ["·","——","——","·","——","——","·"]
        self.board_ret = [self.a,self.b,self.c,self.d,self.e,self.f,self.g]
        # self.count_positions = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
        
    def board_def(self):
        r = 1
        for e in range(0,len(self.board_ret)):
            print(r,end=" ")
            r+=1
            for i in range(0,len(self.board_ret)):
                print(self.board_ret[e][i],end=" ")
            print("")
        print(" ","1"," 2"," 3","4","5"," 6"," 7")
    def elimin(self,file_eliminate,board_e):
        verific_eliminate =[[board_e[0][0],board_e[0][3],board_e[0][6]],
                            [board_e[1][1],board_e[1][3],board_e[1][5]],
                            [board_e[2][2],board_e[2][3],board_e[2][4]],
                            [board_e[3][0],board_e[3][1],board_e[3][2]],
                            [board_e[3][4],board_e[3][5],board_e[3][6]],
                            [board_e[4][2],board_e[4][3],board_e[4][4]],
                            [board_e[5][1],board_e[4][3],board_e[5][5]],
                            [board_e[6][0],board_e[6][3],board_e[6][6]],
                            
                            
                            [board_e[1][1],board_e[3][1],board_e[5][1]],
                            [board_e[0][0],board_e[3][0],board_e[6][0]],
                            [board_e[2][2],board_e[3][2],board_e[4][2]],
                            [board_e[0][3],board_e[1][3],board_e[2][3]],
                            [board_e[4][3],board_e[5][3],board_e[6][3]],
                            [board_e[2][4],board_e[3][4],board_e[4][4]],
                            [board_e[1][5],board_e[3][4],board_e[5][5]],
                            [board_e[0][6],board_e[3][6],board_e[6][6]]]
        for e in range(0,len(verific_eliminate)):
            if (file_eliminate.simbol,file_eliminate.simbol,file_eliminate.simbol) == (verific_eliminate[e][0],verific_eliminate[e][1],verific_eliminate[e][2]):
                # conten = verific_eliminate.pop(e)
                return True