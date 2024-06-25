"""
这是由 Fesdrer 独立编写的测试数据批量生成库。
"""
import os
import copy
import random

class IOData:
	"""
	核心类，代表一道题目的测试数据。
	"""
	def __init__(self,datanum:list):
		"""
		datanum 是 InGeneration 需要读入的数据，按照列表顺序读入，列表中每个元素都应为二元组。

		例如， InGeneration 需要读入数据范围 (1,1000) 和数据组数 t ，则 list 应为 [('n',(1,1000)),('t',5)]。
		"""
		self.datanumber={}
		self.basedatanumber={}
		self.outputlist=[]
		for i in datanum:
			self.datanumber[i[0]]=i[1]
			self.basedatanumber[i[0]]=i[1]
			self.outputlist.append(i[0])
	def NumberChange(self,number:list=[]):
		"""
		list 是临时改变的数据。
		"""
		self.datanumber=copy.copy(self.basedatanumber)
		for i in number:
			self.datanumber[i[0]]=i[1]
	def NumberBack(self):
		"""
		撤销数据改变操作。
		"""
		self.datanumber=copy.copy(self.basedatanumber)
	def printstr(self):
		"""
		按照顺序返回 datanum 的数据的字符串。
		"""
		ret=''
		for i in self.outputlist:
			if type(self.datanumber[i])==list or type(self.datanumber[i])==tuple:
				for j in self.datanumber[i]:
					ret=ret+str(j)+'\n'
			else:
				ret=ret+str(self.datanumber[i])+'\n'
		return ret
	def CreateCommon(self,InGeneration:str,Std:str):
		"""
		普通地返回一个测试数据
		"""
		with open("FIOst.txt","w") as files:
			files.write(self.printstr())
		os.system(InGeneration+" < FIOst.txt > FIOin.txt")
		os.system(Std+" < FIOin.txt > FIOout.txt")
		with open('FIOin.txt','r') as file1:
			ret1=file1.read()
		with open('FIOout.txt','r') as file2:
			ret2=file2.read()
		os.system('del FIOst.txt FIOin.txt FIOout.txt')
		return (ret1,ret2)
	def CreateCheck(self,InGeneration:str,Std:str,WrongStd:str):
		"""
		返回一个测试数据使得其在 WrongStd 上 WrongAnswer
		"""
		with open("FIOst.txt","w") as files:
			files.write(self.printstr())
		while True:
			os.system(InGeneration+" < FIOst.txt > FIOin.txt")
			os.system(Std+" < FIOin.txt > FIOans.txt")
			os.system(WrongStd+" < FIOin.txt > FIOout.txt")
			if os.system('fc FIOans.txt FIOout.txt')==1:
				break
		with open('FIOin.txt','r') as file1:
			ret1=file1.read()
		with open('FIOans.txt','r') as file2:
			ret2=file2.read()
		os.system('del FIOst.txt FIOin.txt FIOout.txt FIOans.txt')
		return (ret1,ret2)


def CreateMore(operation:list):
	"""
	返回一个多测数据，输入输出名称为 Inname Outname。

	operation 为一个数组，每个元组都是一个二元列表 [a:int,b:Function]，表示多测的其中 a 组用 b 来生成。

	其中 a 可以是一个整数，也可以是一个二元组表示数量在其中随机生成。

	b 作为一组数据的生成函数，有且仅有两个调用数据：输入输出名称。
	"""
	sum=0
	for now in operation:
		sum=sum+now[0]
	ret1=str(sum)+'\n'
	ret2=''
	for now in operation:
		if type(now[0])==list:
			now[0]=random.randint(now[0][0],now[0][1])
		for i in range(0,now[0]):
			testdata=now[1]()
			ret1=ret1+testdata[0]+'\n'
			ret2=ret2+testdata[1]+'\n'
	return (ret1,ret2)


def IO(problemname:str,ranges,rangestr:int,CreateFunction,problemend='.ans'):
	"""
	批量生成测试数据。

	problemname 是题目名称， ranges 为数据编号，可以是一个整数也可以是一个二元组表示区间， rangestr 为数据编号表示方法。
	
	例如 problemname='num' 的第一个测试点， rangestr 为 1 为 num1.in ，为 2 为 num01.in ，为 3 为 num001

	其中 CreateFunction 为一组数据的生成函数，有且仅有两个调用数据：输入输出名称。

	problemend 是输出数据的类型，如 .ans .out
	"""
	def to_str(x):
		if rangestr==3:
			return str(int(x/100))+str(int(x/10)%10)+str(x%10)
		elif rangestr==2:
			return str(int(x/10)%10)+str(x%10)
		return str(x)
	if type(ranges)==int:
		ranges=(ranges,ranges)
	for j in range(ranges[0],ranges[1]+1):
		testdata=CreateFunction()
		with open(problemname+to_str(j)+'.in','w') as files:
			files.write(testdata[0])
		with open(problemname+to_str(j)+problemend,'w') as files:
			files.write(testdata[1])


def CheckIO(problemname:str,ranges,rangestr:int,Std:str,problemend='.ans'):
	def to_str(x):
		if rangestr==3:
			return str(int(x/100))+str(int(x/10)%10)+str(x%10)
		elif rangestr==2:
			return str(int(x/10)%10)+str(x%10)
		return str(x)
	if type(ranges)==int:
		ranges=(ranges,ranges)
	wrong=[]
	for i in range(ranges[0],ranges[1]+1):
		Infile=problemname+to_str(i)+'.in'
		Outfile=problemname+to_str(i)+problemend
		os.system(Std+' < '+Infile+' > FIOcheckans.txt')
		if os.system('fc '+Outfile+' FIOcheckans.txt')==1:
			wrong.append(i)
	os.system('del FIOcheckans.txt')
	return wrong


def ClearEmptyLine(problemname:str,ranges,rangestr:int,problemend='.ans'):
	def to_str(x):
		if rangestr==3:
			return str(int(x/100))+str(int(x/10)%10)+str(x%10)
		elif rangestr==2:
			return str(int(x/10)%10)+str(x%10)
		return str(x)
	def clear(filename):
		with open(filename, 'r') as f_input, open('FClear.txt', 'w') as f_output:
			for line in f_input:
				if line.strip():
					f_output.write(line)
		os.system('del '+filename)
		os.system('ren FClear.txt '+filename)
	if type(ranges)==int:
		ranges=(ranges,ranges)
	wrong=[]
	for i in range(ranges[0],ranges[1]+1):
		Infile=problemname+to_str(i)+'.in'
		Outfile=problemname+to_str(i)+problemend
		clear(Infile)
		clear(Outfile)
	return wrong
