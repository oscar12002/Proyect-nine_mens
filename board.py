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
        
    def board_def(self):
        r = 1
        for e in range(0,len(self.board_ret)):
            print(r,end=" ")
            r+=1
            for i in range(0,len(self.board_ret)):
                print(self.board_ret[e][i],end=" ")
            print("")
        print(" ","1"," 2"," 3","4","5"," 6"," 7")
        
    def elimin(self,file_eliminate,board_e,verify):
        for e in range(0,len(verify)):
            if (file_eliminate.simbol,file_eliminate.simbol,file_eliminate.simbol) == (verify[e][0],verify[e][1],verify[e][2]):
                conten = verify.pop(e)
                return True