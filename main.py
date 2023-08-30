import gui


def main() -> None:
	window_size, white, black = (640, 640), (255, 255, 255), (0, 0, 0)
	size_of_board_square = 80

	start = gui.GuidedUI(window_size, black, white, size_of_board_square)
	start.run()


if __name__ == "__main__":
	main()
