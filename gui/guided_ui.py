import pygame
import chess

from gui.board import Board


class GuidedUI:
	def __init__(self, window_size: tuple, chess_engine: chess.Board):
		self.board = Board(board_size=window_size, chess_engine=chess_engine)
		self.window_size = window_size


	def run(self) -> None:
		"""
		Start main GUI process that updates screen
		"""
		running = True

		pygame.display.set_caption("ML CHESS")
		pygame.init()
		screen = pygame.display.set_mode(self.window_size)
		surface = pygame.Surface((screen.get_width(), screen.get_height()))

		# Create clock to calculate the FPS.
		clock = pygame.time.Clock()

		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					# Stop running if pygame window closed.
					running = False
				elif event.type == pygame.MOUSEBUTTONDOWN:
					print(event.pos)

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
