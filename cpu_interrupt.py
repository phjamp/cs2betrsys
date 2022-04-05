#!/usr/bin/python3

import threading
import time

interrupt_interval=5 # in Sekunden

# ACHTUNG:
# * `interrupt` ist "Shared State"!
# * ... und ist *nicht* synchronisiert!
# * -> das ist *nicht* korrekt!
#
interrupt=False
stack=[]
pc=0

def interrupt_controller_thread():
  while True:
    global interrupt
    time.sleep(interrupt_interval)
    print("Triggering interrupt")
    interrupt=True

def cpu_handle_interrupt():
    global interrupt
    global stack
    global pc
    if interrupt == True:
      print("Woah I got an interrupt")
      # now act on the interrupt...
      stack.append(pc)
      pc = 11
      print("stack.push: ",stack[-1])
      print("interrupt handler in Assembler")
      interrupt = False

def cpu_thread():
    global pc 
    NOP = 'NOP'
    JMP = 'JMP'
    IR = 'IR'
    IRET = 'IRET'
    programm = [NOP, NOP, JMP, 4, NOP, NOP, NOP, NOP, NOP, JMP, 0, IR, NOP, IRET]
    while True:
         # Read, Eval, (optional: Print), Loop
        op = programm[pc]
        print("pc in CPU thread: ",pc)
        if(op == NOP):
            print(NOP)
            pc += 1
        elif(op == JMP):
            jmptarget = programm[pc+1]
            assert isinstance(jmptarget,int)
            assert jmptarget >= 0 and jmptarget < len(programm) and jmptarget != pc+1
            print(JMP)
            pc = jmptarget
        elif(op == IR):
            print(IR)
            pc += 1
        elif(op == IRET):
            print(IRET)
            pc=stack.pop()
            print("stack pop: ",pc)
        else:
            print("unknown")
            pc += 1
        time.sleep(1) # python threading doesn't really work
        cpu_handle_interrupt()

cpu = threading.Thread( target = cpu_thread )
pic = threading.Thread( target = interrupt_controller_thread )

cpu.start()
pic.start()

cpu.join()
pic.join()
