#Здесь у нас происходят все возможные заполнения массивов, конфигов и т. д.

import random


def randxy(amount, lines, columns, board, output):
	for z in range(amount):
		y = random.randint(0, lines)
		x = random.randint(0, columns)
		board[y][x] = output

class main:
	
	def __init__(self, lines, columns, board):
		self.lines = lines - 1
		self.columns = columns - 1
		self.board = board
	
	def cell(self, amount):
		randxy(amount, self.lines, self.columns, self.board, 1)