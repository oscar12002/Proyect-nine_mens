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
