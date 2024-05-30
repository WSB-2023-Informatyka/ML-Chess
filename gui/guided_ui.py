from enum import StrEnum, auto
from typing import Optional
import numpy as np

import chess
import pygame
from pygame.font import Font

from ai import AI
from gui.board import Board


class State(StrEnum):
	OK = "OK"
	InvalidMove = "Invalid Move"


class GuidedUI:


	def __init__(self, window_size: tuple, chess_engine: chess.Board, simulation=None):
		self.board = Board(board_size=window_size, chess_engine=chess_engine)
		self.window_size = window_size
		self.font: Optional[Font] = None
		self.font_size = int(self.window_size[0] / 16)

		self.players_turn = True
		self.simulation = simulation

		self.is_figure_selected = False
		self.selected_figure_position: Optional[str] = None
		self.move: Optional[chess.Move] = None
		self.state = State.OK





	def handle_event(self) -> bool:
		"""
		Handling event and return True if a move is recorded, otherwise return False.
		"""
		change = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				# Stop running if pygame window closed.
				self.running = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if self.state != State.OK:
					self.state = State.OK
				change = True
				self.handle_mouseclick(event.pos)

		return change

	def handle_mouseclick(self, position: tuple[int, int]) -> None:
		if not self.is_figure_selected:
			self.selected_figure_position = self.board.translate_from_coords(position)
			self.is_figure_selected = True

			return None
		else:
			self.is_figure_selected = False
			move_from = self.selected_figure_position
			move_to = self.board.translate_from_coords(position)

			if move_from and move_to:
				self.handle_move(move_from, move_to)

	def handle_move(self, move_from: str, move_to: str) -> None:
		if self.board.is_legal_move(move_from, move_to) and self.players_turn:
			self.board.move_piece(move_from, move_to)
			self.players_turn = False
		else:
			self.state = State.InvalidMove

	def run(self, ticks: int, ai: Optional[AI] = None) -> None:
		"""
		Start main GUI process that updates screen
		"""
		self.running = True

		pygame.display.set_caption("ML CHESS")
		pygame.init()
		self.font = pygame.font.Font(
			"./assets/SpaceMono-Regular.ttf", size=self.font_size)
		screen = pygame.display.set_mode(self.window_size)

		# Create clock to calculate the FPS.
		clock = pygame.time.Clock()

		first_frame = True
		ticker = 0
		force_render = False

		while self.running:
			# Check if move was done, if yes, then render the new board state.
			if self.simulation:
				ticker += 1
				if ticker == ticks:
					ticker = 0
					move = next(self.simulation, -1)
					if move == -1:
						self.simulation = None
					elif type(move) is chess.Move:
						self.board.move_piece(move=move)
						force_render = True

			if ai:
				while not self.players_turn:
					try:
						move = ai.move(str(self.board.engine))
						self.board.move_piece(move=move)
						self.players_turn = True
						force_render = True
					except Exception as e:
						print(e)
			else:
				self.players_turn = True

			if self.handle_event() or first_frame or force_render:
				if first_frame:
					first_frame = False
				if force_render:
					force_render = False

				surface = pygame.Surface(
					(screen.get_width(), screen.get_height()))

				# Enable if needed, to display the FPS in console.
				# print(clock.get_fps())

				# Fill the surface with new contents.
				self.board.draw(surface)

				if self.state in (State.InvalidMove) and self.font:
					message = self.font.render(self.state, True, "red")
					pos = (0, 0)
					surface.blit(message, pos)

				# Draw the surface to buffer.
				screen.blit(surface, (0, 0))
				# And update the screen with contents of buffer.
				pygame.display.update()

			# Lock the FPS to 60.
			clock.tick(60)

		pygame.quit()
