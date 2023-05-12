import GUI


def main() -> None:
	WINDOW_SIZE = (700, 700)
	WHITE, BLACK = (255, 255, 255), (0, 0, 0)

	start = GUI.GuidedUI(WINDOW_SIZE, BLACK, WHITE)
	start.run()


if __name__ == "__main__":
	main()
