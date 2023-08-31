import pygame
import chess

from gui.pieces import Pawn


BLACK_SQUARE_COLOR = (0, 0, 0)
WHITE_SQUARE_COLOR = (255, 255, 255)


class Board():
	def __init__(self, board_size: tuple, chess_engine: chess.Board) -> None:
		self.board_size = board_size
		self.engine = chess_engine
		self.Pieces = []
		# for i in range(0, 8):
			# self.Pieces.append(Pawn("black"), 0+80*i, 81)
			# self.Pieces.append(Pawn("white"), 0+80*i, 640-160+1)

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

	def draw(self, surface: pygame.surface.Surface) -> None:
		"""
		Draw chessboard on screen
		"""

		rect_size = (self.board_size[0]/8, self.board_size[1]/8)
		surface.fill(WHITE_SQUARE_COLOR)

		for i in range(0, 8):
			for j in range(0, 8):
				if (i + j) % 2 == 0:
					pygame.draw.rect(surface, BLACK_SQUARE_COLOR,
									(i * rect_size[0], j * rect_size[1], rect_size[0], rect_size[1]))

		# TODO: draw all pieces on surface
