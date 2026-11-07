# This file simulates Rule 110 on finite-size field with helical boundary conditions.

from collections import deque
from PIL import Image


console_output = True
console_1 = "##"
console_0 = "  "

img_output = True
img_path = "output.bmp"

height = 66


# One 1
board = "00000000000000000000000000000000000000000000000000000000000000000010"

# Glider E (width=67)
# board = "11111000100110111110001001101111100010011011111000100111110011011111"

# Glider E3 (width=67)
# board = "00010011011111000100110111110001001101111100010011001000111001100010"

# Gliders C1, C2, C1 (width=67)
# board = "10111110001000110001001101111101001110011011111000100011000100110111"


width = len(board) - 1
board = deque([int(c) for c in board])

res = []
for j in range(height):
    for i in range(width):
        new_cell = 0 if ((not board[1]) and (not board[2])) or (board[0] and board[1] and board[2]) else 1
        board.append(new_cell)
        last = board.popleft()
        if console_output:
            print(console_1 if last else console_0, end="")
        res.append(last)
    if console_output:
        print()

if img_output:
    img = Image.new('1', (width, height))
    img.putdata([1-i for i in res])
    img.save(img_path)
