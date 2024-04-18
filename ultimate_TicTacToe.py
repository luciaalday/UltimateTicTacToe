'''
    author: Lucia Alday
    dates worked on: I could not tell you but mostly made after csc110 and then 
    revisited after csc210
'''

#yes this is gonna make me die inside
#but i swear i know what im doing i made a drawwing and everything

#i could just define variables but i will not make a 2D list with 90 ' ' variables on my own
#lmao apparently that's what was fucking up the code but now its ok bc i didnt count i copy pasted

#ok there is a known not solved edge case which is there is an infinite loop if a square is full
#on the bright side full squares are distinguishable
#need to add a way to check that wins are possible to prevent playing to the end for no reason
def board_list():
    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 0, 0, 0, [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    return board

def turns(b):
    #b[10] is for turn number, even ==> X odd ==> O
    #b[11] is for the last O play, aka which big square X goes in
    oplay = b[11]
    xplay = b[12]
    #b[12] is last X play, treat just like b[11] but for O
    if b[10] == 0:
        oplay = int(input('Enter desired square to commence gameplay within:\n'))
    move = 'invalid'
    if b[10] % 2 == 0:
        current_turn(oplay)
        while move == 'invalid':
            # check that square isn't full before asking for play in that square
            # does not work
            # FIX ME
            if b[13][oplay] == 'f':
                oplay = int(input('Enter desired square to continue gameplay witihn:\n'))
                current_turn(oplay)
            xplay = int(input('Enter placement of next X:\n'))
            if b[oplay][xplay] == ' ' and xplay < 9:
                b[oplay][xplay] = 'X'
                move = 'valid'
            else:
                print('Invalid move. Try again.')
    else:
        current_turn(xplay)
        while move == 'invalid':
            if b[13][xplay] == 'f':
                xplay = int(input('Enter desired square to continue gameplay witihn:\n'))
                current_turn(xplay)
            oplay = int(input('Enter placement of next O:\n'))
            if b[xplay][oplay] == ' ' and oplay < 9:
                b[xplay][oplay] = 'O'
                move = 'valid'
            else:
                print('Invalid move. Try again\n')
    b[11] = oplay
    b[12] = xplay
    b[10] += 1
    return b

def check_win(b):
    for i in range(0, 9):
        # change values of b[9] to keep track of local wins
        # check all instances involving the center
        if b[13][i] == ' ':
            # check if square is full
            if ' ' not in b[i]:
                b[9][i] = 'f'               # f is for full
                b[13][i] = 'f'
            if (b[i][4] == b[i][0] and b[i][0] == b[i][8]) or (b[i][4] == b[i][1] and b[i][1] == b[i][7]) or (b[i][4] == b[i][2] and b[i][2] == b[i][6]) or (b[i][4] == b[i][3] and b[i][3] == b[i][5]):
                if b[i][4] == 'O':
                        b[9][i] = 'O'
                elif b[i][4] == 'X':
                    b[9][i] = 'X'
            # check any instances left involving 0 (top left)
            if (b[i][0] == b[i][1] and b[i][1] == b[i][2]) or (b[i][0] == b[i][3] and b[i][3] == b[i][6]):
                if b[i][0] == 'O':
                    b[9][i] = 'O'
                elif b[i][0] == 'X':
                    b[9][i] = 'X'
            # check any instances left (involves 8 (bottom right))
            if (b[i][8] == b[i][5] and b[i][5] == b[i][2]) or (b[i][8] == b[i][7] and b[i][7] == b[i][6]):
                if b[i][8] == 'O':
                    b[9][i] = 'O'
                elif b[i][8] == 'X':
                    b[9][i] = 'X'
        # check if game over          
        if (b[9][4] == b[9][0] and b[9][4] == b[9][8]) or (b[9][4] == b[9][1] and b[9][4] == b[9][7]):
            if b[9][4] == 'O':
                print('O wins! Suck it X')
                return True
            elif b[9][4] == 'X':
                print('X wins! O womp womp')
                return True
        elif (b[9][0] == b[9][1] and b[9][1] == b[9][2]) or (b[9][0] == b[9][3] and b[9][3] == b[9][6]):
            if b[9][0] == 'O':
                print('O wins! No clout for X')
                return True
            elif b[9][0] == 'X':
                print('X wins! Rip O lmao')
                return True
        elif (b[9][8] == b[9][5] and b[9][5] == b[9][2]) or (b[9][8] == b[9][7] and b[9][7] == b[9][6]):
            if b[9][8] == 'O':
                print('O wins! Get better for next time X')
                return True
            elif b[9][8] == 'X':
                print('X wins! Try thinking ahead O')
                return True
        # checks for a tie
        elif ' ' not in b[9]:
            print('It\'s a tie! One of you needs to get better at this')
            return True      
    return False

def print_board(b):
    bare_skeleton = ' ' * 12 + '|' + ' ' * 13 + '|'
    inner_bare = ' ' * 3 + '|' + ' ' * 3 + '|' + ' ' * 4 + '|' + ' ' * 4 + '|' + ' ' * 3 + '|' + ' ' * 4 + '|' + ' ' * 4 + '|' + ' ' * 3 + '|'
    inner_skeleton = '_' * 3 + '|' + '_' * 3 + '|' + '_' * 3 + ' | ' + '_' * 3 + '|' + '_' * 3 + '|' + '_' * 3 + ' | ' + '_' * 3 + '|' + '_' * 3 + '|' + '_' * 3
    outer_skeleton = '_' * 12 + '|' + '_' * 13 + '|' + '_' * 12
    print(bare_skeleton)
    print(' ' + b[0][0] + ' | ' + b[0][1] + ' | ' + b[0][2] + '  |  ' + b[1][0] + ' | ' + b[1][1] + ' | ' + b[1][2] + '  |  ' + b[2][0] + ' | ' + b[2][1] + ' | ' + b[2][2])
    print(inner_skeleton)
    print(' ' + b[0][3] + ' | ' + b[0][4] + ' | ' + b[0][5] + '  |  ' + b[1][3] + ' | ' + b[1][4] + ' | ' + b[1][5] + '  |  ' + b[2][3] + ' | ' + b[2][4] + ' | ' + b[2][5])
    print(inner_skeleton)
    print(' ' + b[0][6] + ' | ' + b[0][7] + ' | ' + b[0][8] + '  |  ' + b[1][6] + ' | ' + b[1][7] + ' | ' + b[1][8] + '  |  ' + b[2][6] + ' | ' + b[2][7] + ' | ' + b[2][8])
    print(inner_bare)
    print(outer_skeleton)
    print(bare_skeleton)
    print(' ' + b[3][0] + ' | ' + b[3][1] + ' | ' + b[3][2] + '  |  ' + b[4][0] + ' | ' + b[4][1] + ' | ' + b[4][2] + '  |  ' + b[5][0] + ' | ' + b[5][1] + ' | ' + b[5][2])
    print(inner_skeleton)
    print(' ' + b[3][3] + ' | ' + b[3][4] + ' | ' + b[3][5] + '  |  ' + b[4][3] + ' | ' + b[4][4] + ' | ' + b[4][5] + '  |  ' + b[5][3] + ' | ' + b[5][4] + ' | ' + b[5][5])
    print(inner_skeleton)
    print(' ' + b[3][6] + ' | ' + b[3][7] + ' | ' + b[3][8] + '  |  ' + b[4][6] + ' | ' + b[4][7] + ' | ' + b[4][8] + '  |  ' + b[5][6] + ' | ' + b[5][7] + ' | ' + b[5][8])
    print(inner_bare)
    print(outer_skeleton)
    print(bare_skeleton)
    print(' ' + b[6][0] + ' | ' + b[6][1] + ' | ' + b[6][2] + '  |  ' + b[7][0] + ' | ' + b[7][1] + ' | ' + b[7][2] + '  |  ' + b[8][0] + ' | ' + b[8][1] + ' | ' + b[8][2])
    print(inner_skeleton)
    print(' ' + b[6][3] + ' | ' + b[6][4] + ' | ' + b[6][5] + '  |  ' + b[7][3] + ' | ' + b[7][4] + ' | ' + b[7][5] + '  |  ' + b[8][3] + ' | ' + b[8][4] + ' | ' + b[8][5])
    print(inner_skeleton)
    print(' ' + b[6][6] + ' | ' + b[6][7] + ' | ' + b[6][8] + '  |  ' + b[7][6] + ' | ' + b[7][7] + ' | ' + b[7][8] + '  |  ' + b[8][6] + ' | ' + b[8][7] + ' | ' + b[8][8])
    print(inner_bare)
    print(bare_skeleton)

def example():
    print(' 0 | 1 | 2 ')
    print('___|___|___')
    print(' 3 | 4 | 5 ')
    print('___|___|___')
    print(' 6 | 7 | 8 ')
    print('   |   |   ')

def current_turn(turn):
    if turn == ' ':
        return
    print('Current square of play:')
    s = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    s[turn] = '*'
    print(' ' + s[0] + ' | ' + s[1] + ' | ' +  s[2] + ' ')
    print('___|___|___')
    print(' ' + s[3] + ' | ' + s[4] + ' | ' +  s[5] + ' ')
    print('___|___|___')
    print(' ' + s[6] + ' | ' + s[7] + ' | ' +  s[8] + ' ')
    print('   |   |   ')

def main():
    board = board_list()
    example()
    while check_win(board) != True:
        board = turns(board)
        print_board(board)

main()