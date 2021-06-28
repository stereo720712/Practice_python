try:
  #for Python2
  from Tkinter import *	
except ImportError:
  #for Python3
  from tkinter import *
	

root = Tk()


ui_label = Label(root,text="fuck label",width="30",height="6")
ui_label.pack()
ui_label.mainloop()


