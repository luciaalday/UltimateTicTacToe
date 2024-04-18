def board_list():
    board = []
    square = []
    for n in range(9):
        square.append(' ')
    for n in range(10):
        board.append(square)
    board.append(0)
    board.append(0)
    board.append(0)
    return board

board = board_list()
print(board)

list = [['*', '*', '*', '*', '*', '*', '*', '*', '*'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'], ['k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k'], ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'], ['f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f'], ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'], ['d', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd'], ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'], ['q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q'], 0, 0, 0]
list[2][2] = '%'
print(list[2][2])
print(list)
