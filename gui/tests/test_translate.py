import warnings

import chess

from gui import Board

warnings.filterwarnings("ignore", category=DeprecationWarning,
                        module="pkg_resources")  # mute that warning in tests


def test_Board_translate_to_coords():
	b = Board(board_size=(640, 640), chess_engine=chess.Board())

	coords = b.translate_to_coords('A1')
	assert (0, 560) == coords

	coords = b.translate_to_coords('G3')
	assert (480, 400) == coords

	coords = b.translate_to_coords('C8')
	assert (160, 0) == coords

	coords = b.translate_to_coords('B5')
	assert (80, 240) == coords

	coords = b.translate_to_coords('E2')
	assert (320, 480) == coords

	coords = b.translate_to_coords('H1')
	assert (560, 560) == coords

	coords = b.translate_to_coords(chess.H1)
	assert (560, 560) == coords

	# Rainy-day scenarios:

	coords = b.translate_to_coords('G1')
	assert (560, 560) == coords

	coords = b.translate_to_coords('G9')
	assert (560, 560) == coords

	coords = b.translate_to_coords('G0')
	assert (560, 560) == coords

	coords = b.translate_to_coords(256)
	assert (560, 560) == coords


def test_Board_translate_from_coords():
	b = Board(board_size=(640, 640), chess_engine=chess.Board())

	field = b.translate_from_coords((23, 587))
	assert 'A1' == field

	field = b.translate_from_coords((499, 421))
	assert 'G3' == field

	field = b.translate_from_coords((160, 64))
	assert 'C8' == field

	field = b.translate_from_coords((139, 240))
	assert 'B5' == field

	field = b.translate_from_coords((329, 512))
	assert 'E2' == field

	field = b.translate_from_coords((560, 639))
	assert 'H1' == field

	# Rainy-day scenarios:
	field = b.translate_from_coords((-1, 0))
	assert 'H1' == field

	field = b.translate_from_coords((678, 639))
	assert 'H1' == field
