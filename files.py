class File:
    def __init__(self,simbol):
        self.simbol = simbol
        self.quantl = 4
        self.turn = 0
        
    def file_quantly(self):
        sim_qua = self.simbol * self.quantl
        return sim_qua