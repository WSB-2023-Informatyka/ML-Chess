import pygame


class Piece():
	def __init__(self, Color, position: tuple, size: tuple) -> None:
		self.color = Color
		self.position = position
		self.size = size

	def render(self, surface: pygame.Surface):
		"""
		Render the piece onto the surface.
		"""
		raise Exception("unimplemented")

	def tranlate(self, new_position):
		"""
		Change the position of the piece to new position.
		"""
		raise Exception("unimplemented")

class Pawn(Piece):
	def __init__(self, Color, position: tuple, size: tuple) -> None:
		super().__init__(Color, position=position, size=size)
		with open('path/to/pawn.png') as image: # FIXME: set the correct path
			self.image = image

class Bishop(Piece):
	# TODO: implement this piece;
	pass

class Knight(Piece):
	# TODO: implement this piece;
	pass

class Rook(Piece):
	# TODO: implement this piece;
	pass

class Queen(Piece):
	# TODO: implement this piece;
	pass

class Bishop(Piece):
	# TODO: implement this piece;
	pass

class King(Piece):
	# TODO: implement this piece;
	pass
