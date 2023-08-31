import chess

import gui


def main() -> None:
	window_size = (640, 640)

# TODO: Implement loading data from pgn file. Related to board.py > update_board(self) (line 21)
	board = chess.Board()

	print(board)

	start = gui.GuidedUI(window_size, chess_engine=board)
	start.run()

if __name__ == "__main__":
	main()
