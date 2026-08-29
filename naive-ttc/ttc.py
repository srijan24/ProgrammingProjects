from typing import Any

import helpers


class Board:

    BOARD_HEIGHT = 5
    BOARD_WIDTH = 5
    WIN_LEN = 4
    GAME_SYMBOLS = "xo#@!%$&?ABCDEFGHIJKLMNOPQRS"

    @property
    def BOARD_LENGTH(self):
        return self.BOARD_HEIGHT * self.BOARD_WIDTH

    @property
    def winning_lines(self):
        start_poses = [(w, 0) for w in range(1, self.BOARD_WIDTH)] + [
                (0, h) for h in range(1, self.BOARD_HEIGHT)
                ]
        start_poses += [(w, self.BOARD_HEIGHT - 1) for w in range(self.BOARD_WIDTH - 1)]
        start_poses += [(self.BOARD_WIDTH - 1, h) for h in range(self.BOARD_HEIGHT - 1)]
        start_poses += [(0, 0), (self.BOARD_WIDTH - 1, self.BOARD_HEIGHT - 1)]
        rdiags = []
        ldiags = []
        for w, h in start_poses:
            r, l = [], []
            for ite in range(max(self.BOARD_HEIGHT, self.BOARD_WIDTH)):
                if (0 <= (w + ite) < self.BOARD_WIDTH) and (
                        0 <= (h + ite) < self.BOARD_HEIGHT
                        ):
                    r.append((w + ite, h + ite))
                if (0 <= (w - ite) < self.BOARD_WIDTH) and (
                        0 <= (h + ite) < self.BOARD_HEIGHT
                        ):
                    l.append((w - ite, h + ite))
            rdiags.append(r)
            ldiags.append(l)
        ldiags = [
                tuple(self.state[h * self.BOARD_WIDTH + w] for (w, h) in l) for l in ldiags
                ]
        rdiags = [
                tuple(self.state[h * self.BOARD_WIDTH + w] for (w, h) in r) for r in rdiags
                ]

        cols = [
                tuple(self.state[h :: self.BOARD_WIDTH]) for h in range(self.BOARD_HEIGHT)
                ]
        rows = [
                tuple(self.state[h * self.BOARD_WIDTH : (h + 1) * self.BOARD_WIDTH :])
                for h in range(self.BOARD_HEIGHT)
                ]

        return [*ldiags, *rdiags, *cols, *rows]

    @property
    def won_game(self) -> str | None:
        for dag in self.winning_lines:
            for symb in self.GAME_SYMBOLS:
                if helpers.sub_tuple(tuple(symb * self.WIN_LEN), dag):
                    return symb
        return None

    def __init__(self, state: list[str] | None = None):

        if state is None:
            self.state = [_ for _ in range(self.BOARD_LENGTH)]
        else:
            self.state = state

    def __repr__(self):
        o = [
                str([self.state[h * self.BOARD_WIDTH + w] for w in range(self.BOARD_WIDTH)])
                + "\n"
                for h in range(self.BOARD_HEIGHT)
                ]
        return "".join(o)

    def __str__(self):
        return self.__repr__()

    def update(self, sym: str, w: int, h: int | None = None) -> None | str:
        if h is None:
            self.state[w] = sym
        else:
            self.state[h * self.BOARD_WIDTH + w] = sym

        return self.won_game


class AIBase:
    def make_move():
        raise NotImplementedError

    def reset():
        raise NotImplementedError

    def save():
        raise NotImplementedError

    def load():
        raise NotImplementedError


class RandomAI(AIBase):
    MAX_TRIES = 25
    def __init__(self, board: Board, name: str):
        self.board = board
        self.seed = 12345
        self.name = name

    def make_move(self) -> int:
        import random
        random.seed(self.seed)
        validmove = None
        while not validmove:
            validmove = random.randint(1, self.board.BOARD_LENGTH-1)
            if self.board.state[validmove] in self.board.GAME_SYMBOLS:
                validmove = None
        return validmove

class LearningAI(AIBase):
    pass


class Game:

    N_PLAYER = 2
    AI_PLAYER = 0


    @property
    def next_player(self):
        return self.board.GAME_SYMBOLS[self.turns % self.nplayers]

    def __init__(self, nplayers: int = 2, aplayers: int = 0):
        self.board = Board()
        self.turns = 0
        self.nplayers = nplayers
        self.aplayers = aplayers

    def turn(self, *pos) -> None | str:
        p = self.next_player
        o = self.board.update(p, *pos)
        if o:
            return f"Player {o} won!"
        elif self.turns >= self.board.BOARD_LENGTH:
            return (f"Draw, none of the {self.nplayers} player(s) and "
                    f"none of the {self.aplayers} AI(s) won!")
        self.turns += 1


if __name__ == "__main__":

    def test_basic_functionality():
        b = Board()
        b.won_game
        print(b)

        print(f"Initial State:\n{b}")
        out1 = b.update("x", 2, 1)

        print(f"After ('x', 2, 1) = {out1}:\n{b}")
        out2 = b.update("x", 8)

        print(f"After ('x', 8) = {out2}:\n{b}")

        out3 = b.update("x", 2)
        print(f"After ('x', 2) = {out3}:\n{b}")
        print(b.won_game)

        print(b.winning_lines)
