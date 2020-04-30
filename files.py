class File:
    def __init__(self,simbol,m_simbol):
        self.simbol = simbol
        self.m_simbol = m_simbol
        self.quantl = 4
        self.new_quantl = 0
        self.turn = 0
        
    def file_quantly(self):
        sim_qua = self.simbol * self.quantl
        return sim_qua