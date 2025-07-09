'''
author: Lucia Alday (with some help from contributors Race Williams and Charlie McLaughlin)
file: regular_TicTacToe.py
purpose: make a shorter version than Race (whose min was 12 lines) and demonstrate normal game play of tic tic toe in terminal
'''

b, play, turn = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'O'], 9, 0
print(' 0 | 1 | 2 \n___|___|___\n 3 | 4 | 5 \n___|___|___\n 6 | 7 | 8 \n   |   |   ')
while turn < 9 and turn >= 0 and not (((b[0]==b[4]==b[8] or b[1]==b[4]==b[7] or b[2]==b[4]==b[6] or b[3]==b[4]==b[5]) and b[4] in 'XO')or ((b[0]==b[1]==b[2] or b[0]==b[3]==b[6]) and b[0]in 'XO')or ((b[8]==b[7]==b[6] or b[5]==b[8]==b[2]) and b[8]in 'XO')):
    while play > 8 or b[play] != ' ': play = int(input("Enter placement of next " + b[9] + ": "))
    b[play], b[9], b[10], turn = b[9], b[10], b[9], turn + 1
    print(' '+b[0]+' | '+b[1]+' | '+b[2]+' \n___|___|___\n '+b[3]+' | '+b[4]+' | '+b[5]+' \n___|___|___\n '+b[6]+' | '+b[7]+' | '+b[8]+ ' \n   |   |   ')
print(b[10] + " wins!\n" if (((b[0]==b[4]==b[8] or b[1]==b[4]==b[7] or b[2]==b[4]==b[6] or b[3]==b[4]==b[5]) and b[4] in 'XO')or ((b[0]==b[1]==b[2] or b[0]==b[3]==b[6]) and b[0]in 'XO')or ((b[8]==b[7]==b[6] or b[5]==b[8]==b[2]) and b[8]in 'XO')) else "It's a tie! One of you needs to get better")
