import sys
# cpu
NOP = 'NOP'
JMP = 'JMP'

# Test cases
tcOne = [NOP, NOP, JMP, 4, NOP, NOP, JMP, 0]
tcTwo = [NOP, NOP, JMP, 4, NOP, 'Test', JMP, 0]
tcThree = [NOP, NOP, JMP, 2, NOP, JMP, JMP, 0]
tcFour = [NOP, NOP, NOP, JMP, NOP]
tcFive = [NOP, NOP, JMP, 4]
tcSix = [NOP, NOP, JMP, 3]

"""
Überlegung ungültige JMPs:
    - nach JMP kein INT (tcFour)
    - INT nach JMP: OOB (tcFive) 
    - INT nach JMP gleicher Wert wie INT Pos in array (tcSix)

     ~ evtl. JMP zu Anweisung selber => gibt keinen Error, macht evtl. aber keinen Sinn (tcThree)
"""

programm = tcFour     # Array mit Programm Anweisungen

class Cpu:
    def __init__(self):
        self.pc = 0         # programm counter
        self.op = ''         # aktuelle OP zum Ausführen

    def run(self):
        while(True):
            self.load()
            self.execute()

    def load(self):
        self.op = programm[self.pc]
            
    def execute(self):
        if(self.op == NOP):
            print(NOP)
            self.pc += 1
        elif(self.op == JMP):
            jmptarget = programm[self.pc+1]
            assert isinstance(jmptarget,int)
            assert jmptarget >= 0 and jmptarget < len(programm) and jmptarget != self.pc+1
            print(JMP)
            self.pc = jmptarget
        else:
            print("unknown")
            self.pc += 1
        
cpu = Cpu()
cpu.run()