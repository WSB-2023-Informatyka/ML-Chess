class Piece():
	def __init__(self, Color, x, y) -> None:
		self.color = Color
		self.coordinates = (x, y)

	def render(self):
		raise Exception("unimplemented")

class Pawn(Piece):
	def __init__(self, Color, x, y) -> None:
		super().__init__(Color, x, y)
		with open('path/to/pawn.png') as image: # FIXME: set the correct path
			self.image = image

	def render(self):
		# TODO: render image

		pass

class King(Piece):
	pass

class Board():
	def __init__(self) -> None:
		self.Pieces = []
		for i in range(0, 8):
			self.Pieces.append(Pawn("black"), 0+80*i, 81)
			self.Pieces.append(Pawn("white"), 0+80*i, 640-160+1)

	def translate(self, field: str) -> tuple:
		# TODO:
		# for input do translation:
		# 1. map row to y based on board size
		# 2. map column to x based on board size
		# e.g. field = "G3", board_size = (640, 640)
		# y = 5*80+1 (5 instead of 3, because board rows are counted bottom-to-top, and coords are counted top-to-bootom)
		# x = 6*80+1

		x = 0
		y = 0

		return (x, y)
