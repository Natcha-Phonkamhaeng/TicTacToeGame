# Created 26 Apr 2022
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic Tac Toe Game')
WIDTH = 12
HEIGHT = 4


class App:

	def __init__(self):
		self.clicked = False
		self.x_won = False
		self.o_won = False
		self.count = 0

		self.b1 = Button(root, text='', width=WIDTH, height=HEIGHT, command=lambda: self.click(self.b1))
		self.b2 = Button(root, text='', width=WIDTH, height=HEIGHT, command=lambda: self.click(self.b2))
		self.b3 = Button(root, text='', width=WIDTH, height=HEIGHT, command=lambda: self.click(self.b3))

		self.b4 = Button(root, text='', width=WIDTH, height=HEIGHT, command=lambda: self.click(self.b4))
		self.b5 = Button(root, text='', width=WIDTH, height=HEIGHT, command=lambda: self.click(self.b5))
		self.b6 = Button(root, text='', width=WIDTH, height=HEIGHT, command=lambda: self.click(self.b6))

		self.b7 = Button(root, text='', width=WIDTH, height=HEIGHT, command=lambda: self.click(self.b7))
		self.b8 = Button(root, text='', width=WIDTH, height=HEIGHT, command=lambda: self.click(self.b8))
		self.b9 = Button(root, text='', width=WIDTH, height=HEIGHT, command=lambda: self.click(self.b9))

		# don't use function if you want to start a new game, this will draw a blank grid when new game start
		self.b1.grid(row=0, column=0)
		self.b2.grid(row=0, column=1)
		self.b3.grid(row=0, column=2)

		self.b4.grid(row=1, column=0)
		self.b5.grid(row=1, column=1)
		self.b6.grid(row=1, column=2)

		self.b7.grid(row=2, column=0)
		self.b8.grid(row=2, column=1)
		self.b9.grid(row=2, column=2)

	def click(self, b):
		if b['text'] == '' and self.clicked == False:
			b['text'] = 'X'
			self.clicked = True
			self.count += 1
			self.x_win()			
			if self.x_won:
				self.disabled_btn()
				messagebox.showinfo(title='Tic Tac Toe Game', message='X WON')
				msg = messagebox.askyesno(title='X WON', message='Do You Want To Start New Game?')
				if msg == True:
					# start new game
					app = App()
				elif msg == False:
					root.quit()
		elif b['text'] == '' and self.clicked == True:
			b['text'] = 'O'
			self.clicked = False
			self.count += 1			
			self.o_win()			
			if self.o_won:
				self.disabled_btn()
				messagebox.showinfo(title='Tic Tac Toe Game', message='O WON')
				msg = messagebox.askyesno(title='O WON', message='Do You Want To Start New Game?')
				if msg == True:
					# start new game
					app = App()
				else:
					root.quit()
				
	def x_win(self):
		if self.b1['text'] == 'X' and self.b2['text'] == 'X' and self.b3['text'] == 'X':
			self.b1['bg'] = 'red'
			self.b2['bg'] = 'red'
			self.b3['bg'] = 'red'
			self.x_won = True
		elif self.b4['text'] == 'X' and self.b5['text'] == 'X' and self.b6['text'] == 'X':
			self.b4['bg'] = 'red'
			self.b5['bg'] = 'red'
			self.b6['bg'] = 'red'
			self.x_won = True
		elif self.b7['text'] == 'X' and self.b8['text'] == 'X' and self.b9['text'] == 'X':
			self.b7['bg'] = 'red'
			self.b8['bg'] = 'red'
			self.b9['bg'] = 'red'
			self.x_won = True
		elif self.b1['text'] == 'X' and self.b4['text'] == 'X' and self.b7['text'] == 'X':
			self.b1['bg'] = 'red'
			self.b4['bg'] = 'red'
			self.b7['bg'] = 'red'
			self.x_won = True
		elif self.b2['text'] == 'X' and self.b5['text'] == 'X' and self.b8['text'] == 'X':
			self.b2['bg'] = 'red'
			self.b5['bg'] = 'red'
			self.b8['bg'] = 'red'
			self.x_won = True
		elif self.b3['text'] == 'X' and self.b6['text'] == 'X' and self.b9['text'] == 'X':
			self.b3['bg'] = 'red'
			self.b6['bg'] = 'red'
			self.b9['bg'] = 'red'
			self.x_won = True
		elif self.b3['text'] == 'X' and self.b5['text'] == 'X' and self.b7['text'] == 'X':
			self.b3['bg'] = 'red'
			self.b5['bg'] = 'red'
			self.b7['bg'] = 'red'
			self.x_won = True
		elif self.b1['text'] == 'X' and self.b5['text'] == 'X' and self.b9['text'] == 'X':
			self.b1['bg'] = 'red'
			self.b5['bg'] = 'red'
			self.b9['bg'] = 'red'
			self.x_won = True
		self.tie()

	def o_win(self):
		if self.b1['text'] == 'O' and self.b2['text'] == 'O' and self.b3['text'] == 'O':
			self.b1['bg'] = 'blue'
			self.b2['bg'] = 'blue'
			self.b3['bg'] = 'blue'
			self.o_won = True
		elif self.b4['text'] == 'O' and self.b5['text'] == 'O' and self.b6['text'] == 'O':
			self.b4['bg'] = 'blue'
			self.b5['bg'] = 'blue'
			self.b6['bg'] = 'blue'
			self.o_won = True
		elif self.b7['text'] == 'O' and self.b8['text'] == 'O' and self.b9['text'] == 'O':
			self.b7['bg'] = 'blue'
			self.b8['bg'] = 'blue'
			self.b9['bg'] = 'blue'
			self.o_won = True
		elif self.b1['text'] == 'O' and self.b4['text'] == 'O' and self.b7['text'] == 'O':
			self.b1['bg'] = 'blue'
			self.b4['bg'] = 'blue'
			self.b7['bg'] = 'blue'
			self.o_won = True
		elif self.b2['text'] == 'O' and self.b5['text'] == 'O' and self.b8['text'] == 'O':
			self.b2['bg'] = 'blue'
			self.b5['bg'] = 'blue'
			self.b8['bg'] = 'blue'
			self.o_won = True
		elif self.b3['text'] == 'O' and self.b6['text'] == 'O' and self.b9['text'] == 'O':
			self.b3['bg'] = 'blue'
			self.b6['bg'] = 'blue'
			self.b9['bg'] = 'blue'
			self.o_won = True
		elif self.b3['text'] == 'O' and self.b5['text'] == 'O' and self.b7['text'] == 'O':
			self.b3['bg'] = 'blue'
			self.b5['bg'] = 'blue'
			self.b7['bg'] = 'blue'
			self.o_won = True
		elif self.b1['text'] == 'O' and self.b5['text'] == 'O' and self.b9['text'] == 'O':
			self.b1['bg'] = 'blue'
			self.b5['bg'] = 'blue'
			self.b9['bg'] = 'blue'
			self.o_won = True
		self.tie()

	def disabled_btn(self):
		self.b1['state'] = DISABLED
		self.b2['state'] = DISABLED
		self.b3['state'] = DISABLED
		self.b4['state'] = DISABLED
		self.b5['state'] = DISABLED
		self.b6['state'] = DISABLED
		self.b7['state'] = DISABLED
		self.b8['state'] = DISABLED
		self.b9['state'] = DISABLED

	def draw(self):
		# if you put this in a function, every time you start a new game, you won't be able to start new grid.
		# it will draw the old grid on screen
		self.b1.grid(row=0, column=0)
		self.b2.grid(row=0, column=1)
		self.b3.grid(row=0, column=2)

		self.b4.grid(row=1, column=0)
		self.b5.grid(row=1, column=1)
		self.b6.grid(row=1, column=2)

		self.b7.grid(row=2, column=0)
		self.b8.grid(row=2, column=1)
		self.b9.grid(row=2, column=2)

	def tie(self):
		if self.count == 9 and self.x_won == False and self.o_won == False:
			messagebox.showinfo(title='Tic Tac Toe Game', message='This is a DRAW')
			self.disabled_btn()
			msg = messagebox.askyesno(title='O WON', message='Do You Want To Start New Game?')
			if msg == True:
				# start new game
				app = App()
			else:
				root.quit()


app = App()

root.bind('<Escape>', lambda x:root.quit())
root.mainloop()
