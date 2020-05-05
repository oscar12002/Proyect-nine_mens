class File: # class of files
    def __init__(self, simbol, m_simbol):
        self.simbol = simbol # this simbol is for the normal file
        self.m_simbol = m_simbol # this simbol is for replace the normal file when one widmill is created
        self.quantl = 5
        self.turn = 0
        
    def file_quantly(self): # This function return the quantly of files 
        sim_qua = self.simbol * self.quantl
        return sim_qua