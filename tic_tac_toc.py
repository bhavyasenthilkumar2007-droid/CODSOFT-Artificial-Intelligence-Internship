print("=== Tic Tac Toe ===")

slots = ["1","2","3","4","5","6","7","8","9"]

def board():
    print()
    print(slots[0], "|", slots[1], "|", slots[2])
    print(slots[3], "|", slots[4], "|", slots[5])
    print(slots[6], "|", slots[7], "|", slots[8])
    print()

board()

for turn in range(9):

    if turn % 2 == 0:
        player = "X"
    else:
        player = "O"

    position = int(input(f"Player {player} Enter Position (1-9): "))

    if slots[position-1] != "X" and slots[position-1] != "O":
        slots[position-1] = player
    else:
        print("Position already selected!")
        continue

    board()

print("Game Finished")