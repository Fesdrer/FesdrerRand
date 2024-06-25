import os

def IO(name,ranges,InGeneration,Std,number=[],ansend=".ans"):
	def interger_to_str(x):
		return str(int(x/100))+str(int(x/10)%10)+str(x%10)
	rangenum=len(ranges)
	tag=True
	if len(number)==0:
		tag=False
	for i in range(0,rangenum):
		if type(ranges[i])==int:
			ranges[i]=(ranges[i],ranges[i])
		for j in range(ranges[i][0],ranges[i][1]+1):
			if tag:
				with open("in.txt","w") as files:
					if type(number[i])==list:
						for single_number in number[i]:
							files.write(str(single_number)+'\n')
					else:
						files.write(str(number[i])+'\n')
				os.system(InGeneration+" < in.txt > "+name+interger_to_str(j)+".in")
			else:
				os.system(InGeneration+" > "+name+interger_to_str(j)+".in")
			os.system(Std+" < "+name+interger_to_str(j)+".in > "+name+interger_to_str(j)+ansend)