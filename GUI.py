import pygame


class GuidedUI:
	window_size = (700, 700)
	white, black = (255, 255, 255), (0, 0, 0)
	running = True

	pygame.display.set_caption("My Pygame Window")

	background_color = (255, 255, 255)

	screen = pygame.display.set_mode(window_size)

	back_buffer = pygame.Surface((screen.get_width(), screen.get_height()))

	screen.fill(white)
	back_buffer.fill(white)

	def draw_chessboard(self, surface):
		for i in range(0, 8):
			for j in range(0, 8):
				if (i + j) % 2 == 0:
					pygame.draw.rect(surface, self.black, (i * 87, j * 87, 87, 87))

	def run(self):
		# -----------------------------------------  EVENTS  --------------------------------------------
		while running:

			pygame.init()
			# Stop running if pygame window closed.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False

		# ---------------------------------------  END OF EVENTS ---------------------------------------------------------
		# ---------------------------------------  DRAWING ON BOARD ------------------------------------------------------
	import pygame

	# Initialize Pygame
	pygame.init()

	# Set the width and height of the screen
	size = (700, 500)
	screen = pygame.display.set_mode(size)

	# Set the caption of the window
	pygame.display.set_caption("My Pygame Window")

	# Set the background color
	background_color = (255, 255, 255)

	# Loop until the user clicks the close button
	done = False

	# Main game loop
	while not done:
		# Event processing
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

		# Clear the screen
		screen.fill(background_color)

		# Update the screen
		pygame.display.flip()

	# Quit Pygame
	pygame.quit()
	#
	# 	# Fill the screen with white
	# 	self.screen.fill(self.white)
	#
	# 	# Draw the chess board
	# 	self.draw_chessboard(self.back_buffer)
	#
	# 	# Draw images of chess pieces on chess board
	# 	self.screen.blit(self.back_buffer, (0, 0))
	#
	# 	# Update the display
	# 	pygame.display.flip()
	#
	# # ---------------------------------------- END OF DRAWING ON BOARD ----------------------------------------
	# pygame.quit()
