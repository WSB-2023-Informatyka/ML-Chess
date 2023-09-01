from typing import Any
import pygame

class Piece():
	def __init__(self, position: tuple, size: tuple, is_black: bool = False) -> None:
		# is_black here is ignored, left for compatibility.
		self.position = position
		self.size = size

	def render(self, surface: pygame.Surface):
		"""
		Render the piece onto the surface.
		"""
		# TODO: implement this for each piece type (not for generic piece).
		raise Exception("unimplemented")

class Pawn(Piece):
	def __init__(self, position: tuple, size: tuple, is_black: bool) -> None:
		super().__init__(position=position, size=size)
		# if is_black:
		# 	with open('path/to/black/pawn.png') as image: # FIXME: set the correct path
		# 		self.image = image
		# else:
		# 	with open('path/to/white/pawn.png') as image: # FIXME: set the correct path
		# 		self.image = image

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

class King(Piece):
	# TODO: implement this piece;
	pass

class Factory:
	"""
	Implements factory pattern that allows to generate different pieces based only on the color and symbol of the piece.
	https://refactoring.guru/design-patterns/factory-method
	"""
	def __init__(self) -> None:
		pass

	def __call__(self, symbol: str, position: tuple, size: tuple) -> Piece:
		return {
			'p': Pawn, 'P': Pawn,
			'b': Bishop, 'B': Bishop,
			'n': Knight, 'N': Knight,
			'r': Rook, 'R': Rook,
			'q': Queen, 'Q': Queen,
			'k': King, 'K': King,
		}[symbol](position=position, size=size, is_black=symbol.isupper())
