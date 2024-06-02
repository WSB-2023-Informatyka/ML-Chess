import argparse
import pathlib

import chess
import chess.pgn

import gui
from ai import AI


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pgn", type=str, help="Path to the PGN file")
    parser.add_argument(
        "--simulation_ticks",
        type=int,
        default=20,
        help="Ticks between simulation steps",
    )
    parser.add_argument("--simulate", action="store_true", help="Run game simulation")
    parser.add_argument(
        "--ai", action="store_true", help="Run single player game against AI"
    )
    args = parser.parse_args()

    # if args.ai and args.simulate:
    # 	print("Can't run simulation and AI at the same time!")
    # 	exit(1)

    ai = None
    if args.ai:
        ai = AI(5)


    window_size = (640, 640)

    board = chess.Board()
    simulation = None

    if args.pgn:
        game = read_game(pathlib.Path(args.pgn))
        board = game.board()
        if args.simulate:
            simulation = iter(game.mainline_moves())
        else:
            for move in game.mainline_moves():
                board.push(move)

    start = gui.GuidedUI(window_size, chess_engine=board, simulation=simulation)
    start.run(ticks=args.simulation_ticks, ai=ai)


def read_game(pgn: pathlib.Path) -> chess.pgn.Game:
    if pgn.is_file():
        with open(pgn) as f:
            game = chess.pgn.read_game(f)
            if game:
                return game

    raise FileNotFoundError()


if __name__ == "__main__":
    main()
