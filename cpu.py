import sys
# cpu
NOP = 0
ADD = 1
END = 99

programm = [NOP, NOP, ADD, NOP]        # Array mit Programm Anweisungen

class Cpu:
    def __init__(self):
        self.pc = 0         # programm counter
        self.op = 0         # aktuelle OP zum Ausführen

    def run(self):
        while(True):
            self.load()
            self.execute()

    def load(self):
        if self.pc < len(programm):
            self.op = programm[self.pc]
            self.pc += 1
        else:
            self.op = END
            
    def execute(self):
        if(self.op == NOP):
            print("NOP")
        elif(self.op == END):
            sys.exit('programm finished')
        else:
            print("unknown")

cpu = Cpu()
cpu.run()