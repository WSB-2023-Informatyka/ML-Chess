import pygame
import chess

from gui.pieces import Factory


BLACK_SQUARE_COLOR = (0, 0, 0)
WHITE_SQUARE_COLOR = (255, 255, 255)


class Board():
	def __init__(self, board_size: tuple, chess_engine: chess.Board) -> None:
		self.board_size = board_size
		self.engine = chess_engine
		self.pieces = [] # TODO: loop through pieces to render them on surface. Do this in self.draw (line 72)
		self.factory: Factory = Factory()
		self.update_board()

	def update_board(self) -> None:
		# The approach below will allow us to load the game from any point using just the engine.
		# First, loop through all squares in the board.
		for square in chess.SQUARES_180: # range from 0 to 63
			# Get the piece from engine at square.
			piece = self.engine.piece_at(square)

			# If the piece exists, fill it to the starting location on board.
			if piece:
				# Generate the piece based on the
				self.pieces = self.factory(piece.symbol(), self.translate(square), self.get_piece_size())

	def translate(self, field: str | int) -> tuple:
		# TODO:
		# for input do translation:
		# 1. map row to y based on board size
		# 2. map column to x based on board size
		# e.g. field = "G3", board_size = (640, 640)
		# y = 5*80+1 (5 instead of 3, because board rows are counted bottom-to-top, and coords are counted top-to-bootom)
		# x = 6*80+1
		#
		# support also integer based translation.

		if type(field) == int:
			# TODO: numeric translation using fields described in chess (e.g.) chess.A1
			pass

		if type(field) == str:
			# TODO: string based translation
			pass

		x = 0
		y = 0

		return (x, y)

	def get_piece_size(self) -> tuple:
		return (self.board_size[0]/8, self.board_size[1]/8)

	def draw(self, surface: pygame.surface.Surface) -> None:
		"""
		Draw chessboard on screen
		"""
		self.update_board()
		rect_size = self.get_piece_size()
		surface.fill(WHITE_SQUARE_COLOR)

		for i in range(0, 8):
			for j in range(0, 8):
				if (i + j) % 2 == 0:
					pygame.draw.rect(surface, BLACK_SQUARE_COLOR,
									(i * rect_size[0], j * rect_size[1], rect_size[0], rect_size[1]))

		# TODO: draw all pieces on surface
