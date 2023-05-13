import pygame


class GuidedUI:
	def __init__(self, window_size: tuple, board_color: tuple, background_color: tuple):

		self.window_size = window_size
		self.board_color = board_color
		self.background_color = background_color

	def draw_chessboard(self, surface: pygame.surface.Surface, chessboard_color: tuple) -> None:
		"""
		Draw chessboard on screen
		"""
		for i in range(0, 8):
			for j in range(0, 8):
				if (i + j) % 2 == 0:
					pygame.draw.rect(surface, chessboard_color, (i * 87, j * 87, 87, 87))

	def run(self) -> None:
		"""
		Start main GUI process that updates screen.
		"""
		running = True
		pygame.display.set_caption("ML CHESS")

		pygame.init()

		screen = pygame.display.set_mode(self.window_size)

		back_buffer = pygame.Surface((screen.get_width(), screen.get_height()))

		screen.fill(self.background_color)
		back_buffer.fill(self.background_color)

		while running:

			# Stop running if pygame window closed.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False

			pygame.display.flip()

			self.draw_chessboard(back_buffer, self.board_color)

			screen.blit(back_buffer, (0, 0))

			pygame.display.flip()

	pygame.quit()
