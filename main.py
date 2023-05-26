import GUI


def main() -> None:
	window_size, white, black = (700, 700), (255, 255, 255), (0, 0, 0)
	size_of_board_square = 87

	start = GUI.GuidedUI(window_size, black, white, size_of_board_square)
	start.run()


if __name__ == "__main__":
	main()
