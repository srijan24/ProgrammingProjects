from typing import Any




class AIChoices():
    def __init__(self, given: Any, choices: Any):
        self.given = given
        self.choices = choices
        NotImplementedError("AI not yet developed")

class Board:
    
    BOARD_HEIGHT = 3
    BOARD_WIDTH = 3
    WIN_LEN = 3
    N_PLAYER = 2
    AI_PLAYER = 0
    GAME_SYMBOLS = ['x', 'o']

    @property
    def PLAYERS(self):
        return self.N_PLAYER + self.AI_PLAYER

    @property
    def BOARD_LENGTH(self):
        return self.BOARD_HEIGHT * self.BOARD_WIDTH

    @property
    def won_game(self) -> str | None:
        start_poses = [(w, 0) for w in range(1, self.BOARD_WIDTH)] + [(0, h) for h in range(1, self.BOARD_HEIGHT)] 
        start_poses += [(w, self.BOARD_HEIGHT-1) for w in range(self.BOARD_WIDTH-1)]  
        start_poses += [(self.BOARD_WIDTH-1, h) for h in range(self.BOARD_HEIGHT-1)]
        start_poses += [(0,0), (self.BOARD_WIDTH-1, self.BOARD_HEIGHT-1)]
        rdiags = []
        ldiags = []
        for (w,h) in start_poses:
            r, l = [], []
            for ite in range(max(self.BOARD_HEIGHT, self.BOARD_WIDTH)):
                if (0 <= (w+ite) < self.BOARD_WIDTH) and (0 <= (h+ite) < self.BOARD_HEIGHT):
                    r.append((w+ite, h+ite))
                if (0 <= (w-ite) < self.BOARD_WIDTH) and (0 <= (h+ite) < self.BOARD_HEIGHT):
                    l.append((w-ite, h+ite))
            rdiags.append(r)
            ldiags.append(l)
        ldiags = [tuple(self.state[h*self.BOARD_WIDTH+w] for (w,h) in l) for l in ldiags]
        rdiags = [tuple(self.state[h*self.BOARD_WIDTH+w] for (w,h) in r) for r in rdiags]
        
        cols = [tuple(self.state[h::self.BOARD_WIDTH]) for h in range(self.BOARD_HEIGHT)]
        rows = [tuple(self.state[h*self.BOARD_WIDTH:(h+1)*self.BOARD_WIDTH:]) for h in range(self.BOARD_HEIGHT) ]

        #print(rows)
        #print(cols)
        #print(rdiags)
        #print(ldiags)

        for dag in [*rows, *cols, *rdiags, *ldiags]:
            for symb in self.GAME_SYMBOLS:
                #print((symb)*self.WIN_LEN)
                #print(dag)
                #print()
                if tuple(symb*self.WIN_LEN) == dag: 
                    return symb

        return None




    def __init__(self, state: list[str] | None = None):
        
        if state is None:
            self.state = [_ for _ in range(self.BOARD_LENGTH)]
        else:
            self.state = state

    def __repr__(self):
        o = [str([self.state[h*self.BOARD_WIDTH + w] for w in range(self.BOARD_WIDTH)])+"\n" for h in range(self.BOARD_HEIGHT)]
        return "".join(o) 
    def __str__(self):
        return self.__repr__()

    
    def update_board(self, sym: str, w: int, h: int | None = None) -> None | str:
        if h is None:
            self.state[w] = sym
        else:
            self.state[h*self.BOARD_WIDTH + w] = sym

        return self.won_game




