import ttc

b = ttc.Board()
b.won_game
print(b)

print(f"Initial State:\n{b}")
out1 = b.update_board('x', 2, 1)

print(f"After ('x', 2, 1) = {out1}:\n{b}")
out2 = b.update_board('x', 8)

print(f"After ('x', 8) = {out2}:\n{b}")

out3 = b.update_board('x', 2)
print(f"After ('x', 2) = {out3}:\n{b}")

