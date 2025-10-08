import time
import os

global acc
acc = 0
global pc
pc = 0
global ram
ram = [0]*16384
global output
output = ""
global speed
speed = 1
global log
log = []

# 1 = store
# 2 = load acc
# 3 = input
# 4 = output
# 5 = add
# 6 = subtract
# 7 = branch if 0
# 8 = data
# 9 = ascii value output
# # = halt program


def ALU(adr1, adr2, op):
  if op == 0:
    return adr1+adr2
  elif op == 1:
    return adr1-adr2

def CU(cmd):
  global acc
  global output
  global speed
  global pc
  global log
  #print("excecuting instruction", cmd)
  time.sleep(speed)
  match int(cmd[0]):
    case 1:
      #print(int(cmd[1:].lstrip("0")))
      #print("storing", int(acc), "at address", int(cmd[1:].lstrip("0")))
      ram[int(cmd[1:].lstrip("0"))] = int(acc)
    case 2:
      #print("loading accumulator with value", str(ram[int(cmd[1:].lstrip("0"))]))
      acc = str(ram[int(cmd[1:].lstrip("0"))])
    case 3:
      temp_storage = []
      if cmd[1] == "0" and cmd[2] == "0":
        ram[int(cmd[3:])] = int(input("> "))
      elif cmd[1] == "0" and cmd[2] == "1":
        acc = int(input("> "))
      elif cmd[1] == "1":
        for i in input("> "):
          temp_storage.append(ord(i))
        x = int(cmd[2:])
        for i in temp_storage:
          ram[x] = i
          x += 1
      elif cmd[1] == "2":
        input("> ")
    case 4:
      #print("outputting value", acc)
      output = output + str(acc) + "\n"
    case 5:
      if cmd[1] == "0":
        #print("adding address", int(cmd[2:].lstrip("0")), "and accumulator value ", int(acc.lstrip("0")))
        acc = str(ALU(ram[int(cmd[2:].lstrip("0"))], int(acc.lstrip("0")), 0))
      elif cmd[1] == "1":
        #print("subtracting address", int(cmd[2:].lstrip("0")), "and accumulator value ", int(acc.lstrip("0")))
        acc = str(ALU(ram[int(cmd[2:].lstrip("0"))], int(acc.lstrip("0")), 1))
    case 6:
      #print("clearing output")
      output = ""
    case 7:
      if cmd[1] == "0":
        print(cmd[2:7])
        print(ram[int(cmd[2:7].lstrip("0"))])
        if ram[int(cmd[2:7].lstrip("0"))] == 0:
          pc = int(cmd[7:])
          print("branching to address", cmd[7:])
        else:
          print("branch returned false, not branching")
      else:
        print("yay")
        print(int(cmd[2:7].lstrip("0")))
        print(ram[int(cmd[2:7].lstrip("0"))])
        print(int(cmd[8:13].lstrip("0")))
        print(ram[int(cmd[8:13].lstrip("0"))])
        print(int(cmd[13:].lstrip("0")))
        print(ram[int(cmd[13:].lstrip("0"))])
        #input()
        if ram[int(cmd[2:7].lstrip("0"))] == ram[int(cmd[13:].lstrip("0"))]:
          print("YAY")
          pc = int(cmd[8:13].lstrip("0"))-1
          #time.sleep(1)
        else:
          print("nay")
          #time.sleep(1)
    case 8:
      print("defined data:", int(cmd[1:].lstrip("0")), "| assigning to accumulator")
      acc = str(cmd[1:].lstrip("0"))
    case 9:
      #print("outputting ascii value", int(acc), chr(int(acc)))
      output = output + chr(int(cmd[1:]))

def excecute():
  global pc
  while not(str(ram[pc]) == "#"):
    os.system("clear")
    print(str(ram[pc]))
    #print(ram)
    print(output, end="")
    #print("fetching instruction")
    time.sleep(speed)
    CU(str(ram[pc]))
    pc+=1
    time.sleep(speed)
  os.system("clear")
  print(ram)
  print(pc)
  print("-------------------------")
  print(output)
  print("-------------------------")
  print("program halted")

with open("code.txt", "r+") as f:
  print("compiling...")
  x = 0
  for i in f.readlines():
    if i[0] == "!":
      speed = float(i[1:])
      continue
    if i.replace("\n", "") == "":
      ram[x] = 0
      x+=1
      continue
    if i.replace("\n", "") == "#":
      ram[x] = "#"
      print("#")
      x+=1
      continue
    ram[x] = int(i)
    print(int(i))
    time.sleep(speed)
    x+=1
  input("press enter to excecute\n> ")

excecute()
