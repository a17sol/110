# This file simulates Rule 110 on finite-size field with periodic or constant boundary conditions.

from random import choices
from PIL import Image


console_output = True
console_1 = "##"
console_0 = "  "

img_output = True
img_path = "output.bmp"

periodic = True # True for periodic, False for constant
ghost_cells = 0 # For constant boundary conditions only: the state of the ghost cells outside the board
height = 67


# One 1 (width=67)
board = "0000000000000000000000000000000000000000000000000000000000000000001"

# Ether (width=42)
# board = "110111110001001101111100010011011111000100"

# Gliders demo (width=341)
# board = "00010011011111000100110111110001001101111100010011000100110111110001001101100000100110001001101111100010011001000111110001001101111100011100111000001001101111100010001100001100010011011111000100011000100110111110100111001101111100011101011000100110111110111110001001101110001001101111100010011011111000100110111110001001101111100010011011111"

# Random state (width adjustable)
# board = choices((0, 1), k=100)


width = len(board)
board = [int(c) for c in board]


def step(board, periodic, ghost_cells):
    left, right = (board[-1], board[0]) if periodic else (ghost_cells, ghost_cells)
    tmp = [left, *board, right]
    return [
        0 if ([tmp[i + 1], tmp[i + 2]] == [0, 0] or [tmp[i], tmp[i + 1], tmp[i + 2]] == [1, 1, 1]) else 1
        for i in range(len(board))
    ]

res = []

for _ in range(height):
    res.append(board)
    board = step(board, periodic, ghost_cells)

if console_output:
    for line in res:
        for cell in line:
            print(console_1 if cell else console_0, end="")
        print()

if img_output:
    img = Image.new('1', (width, height))
    img.putdata([1 - cell for line in res for cell in line])
    img.save(img_path)
