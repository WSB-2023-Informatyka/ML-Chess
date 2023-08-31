import chess

import gui


def main() -> None:
	window_size = (640, 640)

	board = chess.Board()

	start = gui.GuidedUI(window_size, chess_engine=board)
	start.run()

if __name__ == "__main__":
	main()
