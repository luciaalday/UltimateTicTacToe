import tkinter as tk
from tkinter import *

def start():
    root = Tk()
    root.title('Tic Tac Toe Start')
    root.config(bg="#ccd1e0")
    root.geometry('300x200')
    
    Label(root, text=' ', bg='#ccd1e0').grid(row=0)
    Label(root, text=' ', bg='#ccd1e0').grid(row=1)
    Label(root, text='Player One Name', bg='#ccd1e0').grid(row=3)
    Label(root, text='Player Two Name', bg='#ccd1e0').grid(row=4)
    e1 = Entry(root)
    e2 = Entry(root)
    e1.grid(row=3, column=1)
    e2.grid(row=4, column=1)
    
    def start_game():
        name1 = e1.get()
        if name1 == '':
            name1 = 'Player 1'
        name2 = e2.get()
        if name2 == '':
            name2 = 'Player 2'
        root.destroy()
        game(name1, name2)
    
    b1 = Button(root, text='Start game!', bg='#ccd1e0', command=lambda:start_game())
    b1.grid(row=5, column=1)
    root.mainloop()

def game(player1, player2):
    board = Tk()
    board.title('Tic Tac Toe')
    board.config(bg='#010101')
    
    global b
    b = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X']
    
    def turn(place, button):
        b[place] = b[9]
        button['state'] = DISABLED
        button['text'] = b[9]
            
        if (((b[0]==b[4]==b[8] or b[1]==b[4]==b[7] or b[2]==b[4]==b[6] or b[3]==b[4]==b[5]) and b[4] in 'XO')or ((b[0]==b[1]==b[2] or b[0]==b[3]==b[6]) and b[0]in 'XO')or ((b[8]==b[7]==b[6] or b[5]==b[8]==b[2]) and b[8]in 'XO')):
            board.destroy()
            end = Tk()
            end.title('Game over')
            winner = player1 if b[9] == 'X' else player2
            Label(end, text= winner + ' wins!').pack(padx=40, pady=60)
            end.mainloop()
        elif ' ' not in b:
            board.destroy()
            end2 = Tk()
            end2.title('Game over')
            Label(end2, text='It\'s a tie! One of you needs to get better at this').pack(padx=40, pady=60)
            end2.mainloop()
        if b[9] == 'X':
            b[9] = 'O'
        else:
            b[9] = 'X'
            
    buttons = []
    for i in range(9):
        buttons.append(Button(board, height=4, width=8))
        buttons[i]['command'] = lambda i=i:turn(i, buttons[i])
        buttons[i].grid(row=i//3, column=(i%3))
    board.mainloop()

def main():
    start()

main()