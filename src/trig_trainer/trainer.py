from .states.base import StateID
from .game import Game

class TrigTrainer:
    def __init__(self) -> None:
        self.total_questions = 0
        self.correct_questions = 0
        self.game = Game()
