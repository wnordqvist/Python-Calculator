from tkinter import *

class Calculator:
	def __init__(self, master):
		self.master = master
		master.title("Python Calculator")

		#screen
		self.screen = Text(master, state='disabled', width=42, height=6, 
		background="gray", foreground="black")

		#positioning screen inside window
		self.screen.grid(row=0, column=0,columnspan=4,padx=5,pady=5)
		self.screen.configure(state='normal')

		#initialize screen as empty
		self.equation =''

		#creating buttons
		b1 = self.createButton('(')
		b2 = self.createButton(')')
		b3 = self.createButton(u"\u03C0"' e')
		b4 = self.createButton('CE')
		b5 = self.createButton(7)
		b6 = self.createButton(8)
		b7 = self.createButton(9)
		b8 = self.createButton(u"\u00F7")
		b9 = self.createButton(4)
		b10 = self.createButton(5)
		b11 = self.createButton(6)
		b12 = self.createButton('x')
		b13 = self.createButton(1)
		b14 = self.createButton(2)
		b15 = self.createButton(3)
		b16 = self.createButton('-')
		b17 = self.createButton(0)
		b18 = self.createButton('.')
		b19 = self.createButton('=')
		b20 = self.createButton('+')
		b21 = self.createButton(u"\u221A")
		b22 = self.createButton('x'u"\u00B2")
		b23 = self.createButton('y'u"\u00B2")
		b24 = self.createButton('EXP')
		b25= self.createButton('SIN')
		b26 = self.createButton('COS')
		b27 = self.createButton('TAN')
		b28 = self.createButton('LOG')
		b29 = self.createButton('ASIN')
		b30 = self.createButton('ACOS')
		b31 = self.createButton('ATAN')
		b32 = self.createButton('LN')

		#buttons stored in list
		buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32]

		#initialize counter
		count = 0
		#arrange buttons in grid
		for row in range(1, 8):
			for column in range(4):
				buttons[count].grid(row=row, column=column)
				count += 1


	def createButton(self,val,write=True,width=4):
		return Button(self.master, text=val, command = lambda:
		self.click(val,write), width=width)

	def click(self,text,write):
		if write == None:
		# this function handles what happens when you click a button
		# 'write' argument if True means the value 'val' should be written on screen, if None, should not be written on screen

			#only evaluate code when there is an equation to be evaluated
			if text == '=' and self.equation: 
				# replace the unicode value of division ./.with python division symbol / using regex
				self.equation= re.sub(u"\u00F7", '/', self.equation)
				print(self.equation)
				answer = str(eval(self.equation))
				self.clear_screen()
				self.insert_screen(answer,newline=True)
			elif text == u"\u232B":
				self.clear_screen()
			
			
		else:
			# add text to screen
			self.insert_screen(text)
		

	def clear_screen(self):
		#to clear screen
		#set equation to empty before deleting screen
		self.equation = ''
		self.screen.configure(state='normal')
		self.screen.delete('1.0', END)

	def insert_screen(self, value,newline=False):
		self.screen.configure(state='normal')
		self.screen.insert(END,value)
		# record every value inserted in screen
		self.equation += str(value)
		self.screen.configure(state ='disabled')

root = Tk()
root.geometry("350x250")
my_gui = Calculator(root)
root.mainloop()

