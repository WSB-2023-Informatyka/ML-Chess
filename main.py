import GUI


def main() -> None:

	WINDOW_SIZE, WHITE, BLACK = (700, 700), (255, 255, 255), (0, 0, 0)
	SIZE_OF_BOARD_SQUARE = 87 # should those constants be in capital letters?

	start = GUI.GuidedUI(WINDOW_SIZE, BLACK, WHITE, SIZE_OF_BOARD_SQUARE)
	start.run()


if __name__ == "__main__":
	main()
