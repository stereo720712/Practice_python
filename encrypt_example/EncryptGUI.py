try:
	#2
	from Tkinter import *
except ImportError:
	#3
	from tkinter import *

from encrypt import Encrypt
import os

class EncryptGUI(Frame):


	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.grid()
		self.createWidgets()
		self.e = None
		self.userInput = ""
		self.result = ""


	def createWidgets(self):
		self.inputText = Label(self)
		self.inputText["text"] = "Input:"
		self.inputText.grid(row=0,column=0)
		self.inputField = Entry(self)
		self.inputField["width"] = 50
		self.inputField.grid(row=0,column=1,columnspan=6)

		self.outputText = Label(self)
		self.outputText["text"] = "Ouptput:"
		self.outputText.grid(row=1,column=0)
		self.outputField = Entry(self)
		self.outputField["width"] = 50
		self.outputField.grid(row=1,column=1,columnspan=6)

		self.new = Button(self)
		self.new["text"] = "New"
		self.new.grid(row = 2 , column = 0)
		self.new["command"] = self.newMethod
		
		self.load = Button(self)
		self.load["text"] = "Load"
		self.load.grid(row = 2 , column = 1)
		self.load["command"] = self.loadMethod
		
		self.save = Button(self)
		self.save["text"] = "Save"
		self.save.grid(row = 2 , column = 2)
		self.save["command"] = self.saveMethod

		self.encode = Button(self)
		self.encode["text"] = "Encode"
		self.encode.grid(row = 2 , column = 3)
		self.encode["command"] = self.encodeMethod

		self.decode = Button(self)
		self.decode["text"] = "Decode"
		self.decode.grid(row = 2 , column = 4)
		self.decode["command"] = self.decodeMethod
		
	
		self.clear = Button(self)
		self.clear["text"] = "Clear"
		self.clear.grid(row = 2 , column = 5)
		self.clear["command"] = self.clearMethod		

		self.copy = Button(self)
		self.copy["text"] = "Copy"
		self.copy.grid(row = 2 , column = 6)
		self.copy["command"] = self.copyMethod

		self.displayText = Label(self)
		self.displayText["text"] = "fucking happend"
		self.displayText.grid(row = 3 , column =0,columnspan=7 )
		
	
	def newMethod(self):

		if self.e == None:
			self.e = Encrypt();
			self.displayText["text"] = self.e

		
	def loadMethod(self):

		if os.path.exists('./code.txt'):
			f = open('./code.txt','r')
			code = f.readline()
			if self.e == None:
				self.e = Encrypt()
			self.e.setCode(code)
			f.closed
			self.displayText["text"] = "code: " + self.e.getCode()
		else:
			self.displayText["text"] = "Load Fail . no code.txt"

	def saveMethod(self):
		
		if self.e == None:
			self.displayText["text"] = "No Encrypt Object"
		else:
			f = open('./code.txt','w')
			f.write(self.e.getCode())
			f.closed
			self.displayText["text"] = "The code is saved"
	
	def encodeMethod(self):
		self.userInput = self.inputField.get()
		if self.userInput == "":
			self.displayText["text"] = "No input"
		else:
			if self.e == None:
				self.displayText["text"] = "No Encrypt Object"
			else:
				self.result = self.e.toEncode(self.userInput)
				self.outputField.delete(0,200)
				self.outputField.insert(0,self.result)
				self.displayText["text"]= "Encoding success"

		
	def decodeMethod(self):
		
		self.userInput = self.inputField.get()
		if self.userInput == "":
			self.displayText["text"] = "No input"
		else:
			if self.e ==None:
				self.displayText["text"] = "No Encrypt Object"
			else:
				self.result = self.e.toDecode(self.userInput)
				self.outputField.delete(0,200)
				self.outputField.insert(0,self.result)
				self.displayText["text"]= "Decoding success"

		
	
	
	def clearMethod(self):
		self.e = None
		self.userInput = ""
		self.result = ""
		self.inputField.delete(0,200)
		self.outputField.delete(0,200)
		self.displayText["text"]= "Clear Success"

	def copyMethod(self):
		
		if self.result == "":
			self.displayText["text"] = "Empty,Copy Failed"
		else:
			self.clipboard_clear()
			self.clipboard_append(self.result)
			self.displayText["text"] = "Encoding Result already copied to clipboard"
	
		
if __name__ == '__main__':
	root = Tk()
	app=EncryptGUI(master=root)
	app.mainloop()




		

		

		
				
	
				
				
				

