import json
import os
from log import *

class cpu:
	def __init__(self):
		# REMINDER: ADD THESE LATER
		self.ram_size = 512
		self.addr_len = len(str(self.ram_size))
		self.nv_mem = None
		self.exec_speed = 0
		self.p_ram = None
		self.p_cmd = None
		self.ram = [0]*self.ram_size
		self.acc = 0
		self.pc = 0
	
	def compile(self, code, addr):

		con=False

		with open(code, "r") as file:
			self.data = json.load(file)
		x = addr
		for z in range(0, len(self.data["program"])):
			for i in self.data["program"][z]:
				if i == "STO":
					self.ram[x] = int("10" + str(self.data["program"][z][i][0]))
				elif i == "LDA":
					self.ram[x] = int("11" + str(self.data["program"][z][i][0]))
				elif i == "INP":
					self.ram[x] = int("20" + str(self.data["program"][z][i][0]))
					if not self.data["program"][z][i][0] == 0:
						self.ram[x] = int(str(self.ram[x]) + str(self.data["program"][z][i][1]) + str(self.data["program"][z][i][2]))
				elif i == "ALU":
					self.ram[x] = int("30" + str(self.data["program"][z][i][0]) + str(self.data["program"][z][i][1]))
					if not(self.data["program"][z][i][0] == 2):
						self.ram[x] = int(str(self.ram[x]) + str(self.data["program"][z][i][2]))
				elif i == "BIZ":
					self.ram[x] = int("31" + str(self.data["program"][z][i][0]) + str(self.data["program"][z][i][1]))
				elif i == "OUT":
					self.ram[x] = 21
				elif i == "ASO":
					self.ram[x] = 22
				elif i == "CLR":
					self.ram[x] = 23
				elif i == "STA":
					self.ram[x] = int("12" + str(self.data["program"][z][i][0]))
				elif i == "HLT":
					self.ram[x] = 99
				else:
					con=True
			if con:
				con=False
				continue
			x += 1
			

	def STO(self, addr):
		addr = int(addr)
		try:
			self.acc = int(self.acc)
		except:
			pass
		if isinstance(self.acc, int) or isinstance(self.acc, float):
			self.ram[addr] = self.acc
		else:
			self.ram[addr] = ord(str(self.acc))

	def LDA(self, addr):
		addr = int(addr)
		self.acc = self.ram[addr]

	def INP(self, _type, addr1=None, addr2=None):
		if int(_type) == 0:
			self.acc = int(input("> "))
		else:
			x = int(addr1)
			for i in input("> "):
				self.ram[x] = ord(i)
				if x == int(addr2):
					break
				else:
					x += 1
	def ALU(self, op, addr1, addr2=None):
		addr1 = int(addr1)
		op = int(op)
		if addr2:
			addr2 = int(addr2)
		if op == 0:
			self.acc = self.ram[addr1] + self.ram[addr2]
		elif op == 1:
			self.acc = self.ram[addr1] - self.ram[addr2]
		elif op == 2:
			self.acc = ~self.ram[addr1]
		elif op == 3:
			self.acc = self.ram[addr1] & self.ram[addr2]
		elif op == 4:
			self.acc = self.ram[addr1] ^ self.ram[addr2]
	
	def BIZ(self, addr1, addr2):
		addr1 = int(addr1)
		addr2 = int(addr2)
		if self.ram[addr1] == 0:
			self.pc = addr2
	
	def OUT(self):
		print(self.acc, end="")
	
	def ASO(self):
		print(chr(self.acc), end="")
	
	def CLR(self):
		os.system("clear")

	def STA(self, val):
		self.acc = val

	def HLT(self):
		self.pc = -2
	
	def run(self):
		init_log()
		while self.pc > -1:
			#print(self.ram)
			#input()
			inst = self.pc
			self.pc += 1
			#print(inst)
			instr = str(self.ram[inst])
			if instr[:2] == "10": # list operations are non inclusive on the higher end
				self.STO(instr[2:])
				log("stored with parameters " + instr[2:])
			elif instr[:2] == "11":
				self.LDA(instr[2:])
				log("loaded accumulator with parameters " + instr[2:])
			elif instr[:2] == "12":
				self.STA(instr[2:])
				log("loaded accumulator with value " + instr[2:])
				log("loaded with parameters " + instr[2:])
			elif instr[:2] == "20":
				try:
					self.INP(instr[2:3], instr[3:self.addr_len+3], instr[self.addr_len+3:2*(self.addr_len+3)])
					log("took input with parameters " + instr[2:3] + " | " + instr[3:self.addr_len+3] + " | " + instr[self.addr_len+3:2*(self.addr_len+3)])
				except:
					self.INP(instr[2:3], instr[3:self.addr_len+3])
					log("took input with parameters " + instr[2:3] + " | " + instr[3:self.addr_len+3])
			elif instr[:2] == "21":
				self.OUT()
				log("output")
			elif instr[:2] == "22":
				self.ASO()
				log("output ascii")
			elif instr[:2] == "23":
				self.CLR()
				log("cleared screen")
			elif instr[:2] == "30":
				self.ALU(instr[2:4], instr[4:self.addr_len+4], instr[self.addr_len+4:2*(self.addr_len+4)])
				log("executed calculation with parameters " + instr[2:4] + " | " + instr[4:self.addr_len+4] + " | " + instr[self.addr_len+4:2*(self.addr_len+4)])
			elif instr[:2] == "31":
				self.BIZ(instr[2:self.addr_len+2], instr[self.addr_len+2:2*(self.addr_len+2)])
				log("branched? with parameters " + instr[2:self.addr_len+2] + " | " + instr[self.addr_len+2:2*(self.addr_len+2)])
			elif instr[:2] == "99":
				self.HLT()
				log("program halted")
