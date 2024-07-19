'''
    author: Lucia Alday
    for regular tic-tac-toe
'''

def turns(b):
    valid = False
    while valid == False:
        if b[9] % 2 == 0:
            xplay = int(input("Enter placement of next X:\n"))
            if xplay < 9 and b[xplay] == ' ':
                valid, b[xplay] = True, 'X'
        else:
            oplay = int(input("Your turn O:\n"))
            if oplay < 9 and b[oplay] == ' ':
                valid, b[oplay] = True, 'O'
    b[9] += 1
    current_turn(b)
    return b

def check_wins(b):
    if (b[0] == b[4] and b[4] == b[8]) or (b[1] == b[4] and b[4] == b[7]) or (b[2] == b[4] and b[4] == b[6]) or (b[3] == b[4] and b[4] == b[5]):
        if b[4] == 'X':
            print("X wins! Womp womp O")
            return True
        elif b[4] == 'O':
            print("O wins! ")
    elif (b[0] == b[1] and b[1] == b[2]) or (b[0] == b[3] and b[3] == b[6]):
        if b[0] == 'X':
            print("X wins!")
            return True
        elif b[0] == "O":
            print("O wins!")
            return True
    elif (b[8] == b[7] and b[7] == b[6]) or (b[8] == b[5] and b[8] == b[2]):
        if b[0] == 'X':
            print("X wins!")
            return True
        elif b[0] == "O":
            print("O wins!")
            return True
    elif ' ' not in b:
        print("It's a tie! One of you needs to get better at this")
        return True
    return False

def current_turn(b):
    print(' ' + b[0] + ' | ' + b[1] + ' | ' +  b[2] + ' ')
    print('___|___|___')
    print(' ' + b[3] + ' | ' + b[4] + ' | ' +  b[5] + ' ')
    print('___|___|___')
    print(' ' + b[6] + ' | ' + b[7] + ' | ' +  b[8] + ' ')
    print('   |   |   ')

def main():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 0]
    current_turn(['0', '1', '2', '3', '4', '5', '6', '7', '8']
    while check_wins(board) != True:
        board = turns(board)

main()
