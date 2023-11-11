import pygame
import chess

from gui.board import Board


class GuidedUI:
	def __init__(self, window_size: tuple, chess_engine: chess.Board):
		self.board = Board(board_size=window_size, chess_engine=chess_engine)
		self.window_size = window_size

	def handle_event(self) -> bool:
		"""
		Handling event and return True if a move is recorded, otherwise return False.
		"""
		change = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				# Stop running if pygame window closed.
				self.running = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				change = True
				print(f'{event.pos} translates to {self.board.translate_from_coords(event.pos)}')
				# TODO: first click, second click
				# TODO: Check if the move is legal, if not then write log to console

		return change

	def run(self) -> None:
		"""
		Start main GUI process that updates screen
		"""
		self.running = True

		pygame.display.set_caption("ML CHESS")
		pygame.init()
		screen = pygame.display.set_mode(self.window_size)
		surface = pygame.Surface((screen.get_width(), screen.get_height()))

		# Create clock to calculate the FPS.
		clock = pygame.time.Clock()

		first_frame = True

		while self.running:
			# Check if move was done, if yes, then render the new board state.
			if self.handle_event() or first_frame:
				if first_frame:
					first_frame = False

				# Enable if needed, to display the FPS in console.
				# print(clock.get_fps())

				# Fill the surface with new contents.
				self.board.draw(surface)

				# Draw the surface to buffer.
				screen.blit(surface, (0, 0))
				# And update the screen with contents of buffer.
				pygame.display.update()

				# Lock the FPS to 60.
			clock.tick(60)

		pygame.quit()
