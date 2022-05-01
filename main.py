# Created 26 Apr 2022
from tkinter import *
from tkinter import messagebox


class Root:

	def __init__(self):
		self.root = Tk()
		self.title = self.root.title('Tic Tac Toe Game')

	def draw(self):
		self.root.bind('<Escape>', lambda x:self.root.quit())
		self.root.mainloop()


class App(Root):	

	def __init__(self, WIDTH=12, HEIGHT=4):
		super().__init__()
		self.frame = Frame(self.root)
		self.end_frame = Frame(self.root)
		self.end_title = Label(self.end_frame, text='End of Game')
		self.clicked = False
		self.x_won = False
		self.o_won = False

		self.b1 = Button(self.frame, text='', width=WIDTH, height=HEIGHT, command=lambda: self.click(self.b1))
		self.b2 = Button(self.frame, text='', width=WIDTH, height=HEIGHT, command=lambda: self.click(self.b2))
		self.b3 = Button(self.frame, text='', width=WIDTH, height=HEIGHT, command=lambda: self.click(self.b3))

		self.b4 = Button(self.frame, text='', width=WIDTH, height=HEIGHT, command=lambda: self.click(self.b4))
		self.b5 = Button(self.frame, text='', width=WIDTH, height=HEIGHT, command=lambda: self.click(self.b5))
		self.b6 = Button(self.frame, text='', width=WIDTH, height=HEIGHT, command=lambda: self.click(self.b6))

		self.b7 = Button(self.frame, text='', width=WIDTH, height=HEIGHT, command=lambda: self.click(self.b7))
		self.b8 = Button(self.frame, text='', width=WIDTH, height=HEIGHT, command=lambda: self.click(self.b8))
		self.b9 = Button(self.frame, text='', width=WIDTH, height=HEIGHT, command=lambda: self.click(self.b9))

	def click(self, b):
		if b['text'] == '' and self.clicked == False:
			b['text'] = 'X'
			self.clicked = True
			self.x_win()
			if self.x_won:
				messagebox.showinfo(title='Tic Tac Toe Game', message='X WON')
				self.frame.destroy()
				self.end()

		elif b['text'] == '' and self.clicked == True:
			b['text'] = 'O'
			self.clicked = False
			self.o_win()
			if self.o_won:
				messagebox.showinfo(title='Tic Tac Toe Game', message='O WON')
				self.frame.destroy()
				self.end()

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

	def end(self):
		self.root.geometry('300x350')
		self.end_frame.pack()
		self.end_title.pack(pady=150)



	def draw_app(self):
		
		self.frame.pack()

		self.b1.grid(row=0, column=0)
		self.b2.grid(row=0, column=1)
		self.b3.grid(row=0, column=2)

		self.b4.grid(row=1, column=0)
		self.b5.grid(row=1, column=1)
		self.b6.grid(row=1, column=2)

		self.b7.grid(row=2, column=0)
		self.b8.grid(row=2, column=1)
		self.b9.grid(row=2, column=2)

		self.draw()

		
def main():
	app.draw_app()

app = App()

if __name__ == '__main__':
	main()
