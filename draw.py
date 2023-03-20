import arcade


class main:
	def __init__(self, lines, columns, pixel_side, BOARD):
		self.lines = lines
		self.columns = columns
		self.BOARD = BOARD
		self.pixel_side = pixel_side

	def draw (self):
		for y in range(self.columns):
			for x in range(self.lines):
				x_board = x * self.pixel_side
				y_board = y * self.pixel_side
				if self.BOARD[x][y] == 1:
					arcade.draw_point(x_board, y_board, (255, 255, 255), self.pixel_side)