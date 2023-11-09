from typing import Any
import pygame


# Load
BLACK_PAWN = pygame.image.load('assets/sense-chess/artwork/pieces/pawn/bP.svg')
BLACK_BISHOP = pygame.image.load('assets/sense-chess/artwork/pieces/bishop/bB.svg')
BLACK_KNIGHT = pygame.image.load('assets/sense-chess/artwork/pieces/knight/bN.svg')
BLACK_ROOK = pygame.image.load('assets/sense-chess/artwork/pieces/rook/bR.svg')
BLACK_QUEEN = pygame.image.load('assets/sense-chess/artwork/pieces/queen/bQ.svg')
BLACK_KING = pygame.image.load('assets/sense-chess/artwork/pieces/king/bK.svg')
WHITE_PAWN = pygame.image.load('assets/sense-chess/artwork/pieces/pawn/wP.svg')
WHITE_BISHOP = pygame.image.load('assets/sense-chess/artwork/pieces/bishop/wB.svg')
WHITE_KNIGHT = pygame.image.load('assets/sense-chess/artwork/pieces/knight/wN.svg')
WHITE_ROOK = pygame.image.load('assets/sense-chess/artwork/pieces/rook/wR.svg')
WHITE_QUEEN = pygame.image.load('assets/sense-chess/artwork/pieces/queen/wQ.svg')
WHITE_KING = pygame.image.load('assets/sense-chess/artwork/pieces/king/wK.svg')


class Piece():
	def __init__(self, position: tuple, size: tuple, is_black: bool = False) -> None:
		# is_black here is ignored, left for compatibility.
		self.position = position
		self.size = size

	def render(self, surface: pygame.Surface):
		"""
		Render the piece onto the surface.
		"""
		raise Exception("unimplemented")

class Pawn(Piece):
	def __init__(self, position: tuple, size: tuple, is_black: bool) -> None:
		super().__init__(position=position, size=size, is_black=is_black)
		if is_black:
			self.image = BLACK_PAWN
		else:
			self.image = WHITE_PAWN
		self.image = pygame.transform.scale(self.image, self.size)

	def render(self, surface: pygame.Surface):
		surface.blit(self.image, self.position)

class Bishop(Piece):
	def __init__(self, position: tuple, size: tuple, is_black: bool = False) -> None:
		super().__init__(position=position, size=size, is_black=is_black)
		if is_black:
			self.image = BLACK_BISHOP
		else:
			self.image = WHITE_BISHOP
		self.image = pygame.transform.scale(self.image, self.size)

	def render(self, surface: pygame.Surface):
		surface.blit(self.image, self.position)

class Knight(Piece):
	def __init__(self, position: tuple, size: tuple, is_black: bool = False) -> None:
		super().__init__(position=position, size=size, is_black=is_black)
		if is_black:
			self.image = BLACK_KNIGHT
		else:
			self.image = WHITE_KNIGHT
		self.image = pygame.transform.scale(self.image, self.size)

	def render(self, surface: pygame.Surface):
		surface.blit(self.image, self.position)

class Rook(Piece):
	def __init__(self, position: tuple, size: tuple, is_black: bool = False) -> None:
		super().__init__(position=position, size=size, is_black=is_black)
		if is_black:
			self.image = BLACK_ROOK
		else:
			self.image = WHITE_ROOK
		self.image = pygame.transform.scale(self.image, self.size)

	def render(self, surface: pygame.Surface):
		surface.blit(self.image, self.position)

class Queen(Piece):
	def __init__(self, position: tuple, size: tuple, is_black: bool = False) -> None:
		super().__init__(position=position, size=size, is_black=is_black)
		if is_black:
			self.image = BLACK_QUEEN
		else:
			self.image = WHITE_QUEEN
		self.image = pygame.transform.scale(self.image, self.size)

	def render(self, surface: pygame.Surface):
		surface.blit(self.image, self.position)

class King(Piece):
	def __init__(self, position: tuple, size: tuple, is_black: bool = False) -> None:
		super().__init__(position=position, size=size, is_black=is_black)
		if is_black:
			self.image = BLACK_KING
		else:
			self.image = WHITE_QUEEN
		self.image = pygame.transform.scale(self.image, self.size)

	def render(self, surface: pygame.Surface):
		surface.blit(self.image, self.position)

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
