import pygame
import chess

from gui.pieces import Factory


BLACK_SQUARE_COLOR = (139, 69, 19)
WHITE_SQUARE_COLOR = (205, 133, 63)


class Board():
	def __init__(self, board_size: tuple, chess_engine: chess.Board) -> None:
		self.board_size = board_size
		self.engine = chess_engine
		self.pieces = []
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
				self.pieces.append(self.factory(piece.symbol(), self.translate_to_coords(square), self.get_piece_size()))

	def translate_to_coords(self, field: str | int) -> tuple:
		max_x, max_y = self.board_size
		size_x, size_y = int(max_x/8), int(max_y/8)
		x = 0
		y = 0

		if type(field) == int:
			field = chess.square_name(field)

		if type(field) == str:
			assert len(field)==2
			field = field.upper()
			row, col = field

			# ASCII code for letter A is 65, so we can subtract 65 to obtain row number
			row = ord(row)-65

			# Start count from A8, so 8 have index 0.
			col = 8-int(col)
			x = row*size_x
			y = col*size_y

		return (x, y)

	def translate_from_coords(self, field: tuple) -> str:
		max_x, max_y = self.board_size
		size_x, size_y = int(max_x/8), int(max_y/8)
		x,y = field

		row = chr(65 + x // size_x)
		col = str(8 - y // size_y)

		return row + col

# TODO: współrzędne ujemne, współrzędne wykraczające poza planszę, pole wykracza poza A-H 1-8, test(XD)

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

		for piece in self.pieces:
			piece.render(surface)
