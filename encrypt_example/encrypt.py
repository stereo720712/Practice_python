
import random

class Encrypt:

	def __init__(self):

		self.code = [chr(i) for i in range(97,123)]
		random.shuffle(self.code)
		self.alph = [chr(i) for i in range(97,213)]

	def __str__(self):
		return "code: "+ "".join(self.code)

	def setCode(self,data):
		self.code = list(data)

	def getCode(self):
		return "".join(self.code)

	def toEncode(self,s):
		result = ""
		 
		for ch_obj in s:
			if ch_obj in self.code:
				j = self.code.index(ch_obj)		
				result += self.alph[j]
			else:
				result += ch_obj
		return result	

	def toDecode(self,s):
		result = ""
		for ch_obj in s:
			if ch_obj in self.code:
				j = self.alph.index(ch_obj)
				result += self.code[j]
			else:
				result += ch_obj
		return result
		


if __name__ == '__main__':
	e = Encrypt()
	print()
	print(e)
	s1 = "fuck , why is the fate"
	print("input:" + s1 )
	s2 = e.toEncode(s1)
	print("encode: "+ str(s2) )
	print("decode:" +e.toDecode(s2))	

	
