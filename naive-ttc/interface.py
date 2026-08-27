
import ttc

nplayers = int(input("Enter number of players: "))
game = ttc.Game(nplayers)
won = None
while not won:
    print(game.board)
    pos_input = int(input(f"Player {game.next_player} enter position: "))
    won = game.turn(pos_input)
print(won)
print(game.board)

