# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 23:52:33 2018

@author: maya
"""

# import
from tkinter import *
import tkinter.messagebox
from random import randint
import time
import numpy as np


# functions
def restartGame(button):
    global currentPlayer
    global x
    global TTTArray
    currentPlayer = x
    TTTArray = np.zeros(shape=[3, 3])
    for s in range(1, 10):
        button[s].config(state=NORMAL, text=' ')


def popupfunc(button, resultString):

    pop = Toplevel(root)
    pop.title("Result")
    frame0 = Frame(pop, bg=c_black, bd=0, relief=FLAT)
    frame0.pack()

    resultTxt = Label(frame0, text=resultString, foreground=c_white,
                      background=c_black, font=('Agency FB', 20))
    resultTxt.grid(row=0, column=0, padx=20, pady=20)

    okButton = Button(frame0, command=pop.destroy, text="OK", width=10, relief=FLAT, bd=0,
                      background=c_black, foreground=c_aqua1, activebackground=c_black, activeforeground=c_black, font=('Agency FB', 20))
    okButton.grid(row=1, column=0, padx=10, pady=0)

    for s in range(1, 10):
        button[s].config(state=DISABLED, disabledforeground=c_aqua3)
#


def displaySelection(button, buttonNumber, numberOfPlayers):
    global currentPlayer
    global o
    global x
    global TTTArray

    positionMapping = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [
        1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}

    currentR, currentC = positionMapping[buttonNumber]
    if currentPlayer == 1:
        button[buttonNumber].config(
            state=DISABLED, disabledforeground=c_aqua1, text="X")
        TTTArray[currentR, currentC] = currentPlayer
        currentPlayer = -1

    else:
        button[buttonNumber].config(
            state=DISABLED, disabledforeground=c_aqua1, text="O")
        TTTArray[currentR, currentC] = currentPlayer
        currentPlayer = 1

    resultScore, resultString = checkForWinner(
        TTTArray.copy(), positionMapping[buttonNumber].copy())
    if resultString != 'Continue':
        popupfunc(button, resultString)
    else:
        if numberOfPlayers == 1:
            alpha, beta = -np.inf, np.inf
            bestMove, resultScore = minimax(TTTArray.copy(), currentPlayer,
                                            positionMapping[buttonNumber], alpha, beta)
            currentR, currentC = bestMove
            buttonNumber = [button for button, move in positionMapping.items() if move == [currentR, currentC]][0]
            if currentPlayer == 1:
                button[buttonNumber].config(
                    state=DISABLED, disabledforeground=c_aqua1, text="X")
                TTTArray[currentR, currentC] = currentPlayer
                currentPlayer = -1

            else:
                button[buttonNumber].config(
                    state=DISABLED, disabledforeground=c_aqua1, text="O")
                TTTArray[currentR, currentC] = currentPlayer
                currentPlayer = 1

        resultScore, resultString = checkForWinner(
            TTTArray.copy(), positionMapping[buttonNumber].copy())
        if resultString != 'Continue':
            popupfunc(button, resultString)


def checkForWinner(board, move):
    currentR, currentC = move
    rSum = board[currentR, :].sum()
    cSum = board[:, currentC].sum()
    dSum = [np.diag(board).sum(), np.diag(np.fliplr(board)).sum()]
    if max([rSum, cSum] + dSum) == 3:
        resultScore = 3
        resultString = "X wins!"
    elif min([rSum, cSum] + dSum) == -3:
        resultScore = -3
        resultString = "O wins!"
    elif np.where(board == 0, 1, 0).sum() == 0:
        resultScore = 0
        resultString = "It's a draw!"
    else:
        resultScore = 999
        resultString = "Continue"
    return resultScore, resultString


def minimax(board, currentPlayer, move, alpha, beta):

    if currentPlayer == 1:
        bestScore = -np.inf
        bestMove = [-1, -1]
    else:
        bestScore = +np.inf
        bestMove = [-1, -1]

    resultScore, resultString = checkForWinner(board, move)
    if resultScore in [3, -3, 0]:
        return [[-1, -1], resultScore]

    emptyCells = np.argwhere(board == 0)
    for emptyCell in emptyCells:
        board[emptyCell[0], emptyCell[1]] = currentPlayer
        move, score = minimax(board, -1 * currentPlayer,
                              emptyCell, alpha, beta)
        board[emptyCell[0], emptyCell[1]] = 0

        if currentPlayer == 1:
            if score > bestScore:
                bestScore = score
                bestMove = emptyCell

            alpha = max(alpha, bestScore)
            if beta <= alpha:
                break

        else:
            if score < bestScore:
                bestScore = score
                bestMove = emptyCell

            beta = min(beta, bestScore)
            if beta <= alpha:
                break
    return bestMove, bestScore


def showXOGrid(numberOfPlayers, frameToHide, headerTxt):
    frameToHide.pack_forget()
    if numberOfPlayers == 1:
        headerTxt.config(text="SINGLEPLAYER GAME")
    elif numberOfPlayers == 2:
        headerTxt.config(text="MULTIPLAYER GAME")

    b = [0 for x in range(0, 10)]
    b[1] = Button(frame2, command=lambda: displaySelection(b, 1, numberOfPlayers), background=c_black, relief=FLAT,
                  bd=0, font=('Agency FB', 45), foreground=c_aqua1, width=4, text="   ", activebackground=c_black)
    b[1].grid(row=1, column=0, padx=0, pady=0)
    b[2] = Button(frame2, command=lambda: displaySelection(b, 2, numberOfPlayers), background=c_black, relief=FLAT,
                  bd=0, font=('Agency FB', 45), foreground=c_aqua1, width=4, text="   ", activebackground=c_black)
    b[2].grid(row=1, column=1, padx=2, pady=0)
    b[3] = Button(frame2, command=lambda: displaySelection(b, 3, numberOfPlayers), background=c_black, relief=FLAT,
                  bd=0, font=('Agency FB', 45), foreground=c_aqua1, width=4, text="   ", activebackground=c_black)
    b[3].grid(row=1, column=2, padx=0, pady=0)
    b[4] = Button(frame2, command=lambda: displaySelection(b, 4, numberOfPlayers), background=c_black, relief=FLAT,
                  bd=0, font=('Agency FB', 45), foreground=c_aqua1, width=4, text="   ", activebackground=c_black)
    b[4].grid(row=2, column=0, padx=0, pady=0)
    b[5] = Button(frame2, command=lambda: displaySelection(b, 5, numberOfPlayers), background=c_black, relief=FLAT,
                  bd=0, font=('Agency FB', 45), foreground=c_aqua1, width=4, text="   ", activebackground=c_black)
    b[5].grid(row=2, column=1, padx=0, pady=0)
    b[6] = Button(frame2, command=lambda: displaySelection(b, 6, numberOfPlayers), background=c_black, relief=FLAT,
                  bd=0, font=('Agency FB', 45), foreground=c_aqua1, width=4, text="   ", activebackground=c_black)
    b[6].grid(row=2, column=2, padx=0, pady=2)
    b[7] = Button(frame2, command=lambda: displaySelection(b, 7, numberOfPlayers), background=c_black, relief=FLAT,
                  bd=0, font=('Agency FB', 45), foreground=c_aqua1, width=4, text="   ", activebackground=c_black)
    b[7].grid(row=3, column=0, padx=0, pady=0)
    b[8] = Button(frame2, command=lambda: displaySelection(b, 8, numberOfPlayers), background=c_black, relief=FLAT,
                  bd=0, font=('Agency FB', 45), foreground=c_aqua1, width=4, text="   ", activebackground=c_black)
    b[8].grid(row=3, column=1, padx=2, pady=0)
    b[9] = Button(frame2, command=lambda: displaySelection(b, 9, numberOfPlayers), background=c_black, relief=FLAT,
                  bd=0, font=('Agency FB', 45), foreground=c_aqua1, width=4, text="   ", activebackground=c_black)
    b[9].grid(row=3, column=2, padx=0, pady=0)
    quitButton = Button(frame3, command=root.destroy, text="QUIT", width=10, relief=FLAT, bd=0, background=c_black,
                        foreground=c_aqua1, activebackground=c_black, activeforeground=c_black, font=('Agency FB', 20))
    quitButton.grid(row=0, column=0, padx=10, pady=0)
    restartButton = Button(frame3, command=lambda: restartGame(b), text="RESTART", width=10, relief=FLAT, bd=0,
                           background=c_black, foreground=c_aqua1, activebackground=c_black, activeforeground=c_black, font=('Agency FB', 20))
    restartButton.grid(row=0, column=1, padx=10, pady=0)



# create root window
root = Tk()


# UI params
# --game window title
gameWindowTitle = "Tic Tac Toe"
# --hex colors
c_black = "#030305"
c_white = "#FFFFFF"
c_aqua1 = "#91FCFF"
c_aqua2 = "#00E7ED"
c_aqua3 = "#007b80"  # greyed out c_aqua1

# modify root window
root.title(gameWindowTitle)
root.configure(background=c_black)


# frames
frame0 = Frame(root, bg=c_black, bd=0, relief=FLAT)
frame0.pack(padx=0, pady=0)
frame1 = Frame(root, bg=c_aqua2, bd=0, relief=FLAT)
frame1.pack(padx=0, pady=0)
frame2 = Frame(root, bg=c_aqua2, bd=0, relief=FLAT)
frame2.pack(padx=70, pady=0)
frame3 = Frame(root, bg=c_black, bd=0, relief=FLAT)
frame3.pack(padx=0, pady=30)


# text
headerTxt = Label(frame0,
                  text='SELECT GAME TYPE:',
                  foreground=c_white,
                  background=c_black,
                  font=('Agency FB', 25))

headerTxt.grid(row=0,
               column=0,
               columnspan=3,
               padx=20,
               pady=20)

b = [0] * 5
# empty button for spacing
b[0] = Button(frame1,
              text='\n',
              background=c_black,
              bd=0,
              font=('Agency FB', 15),
              foreground=c_aqua1,
              width=5,
              activebackground=c_black)
b[0].grid(row=1, column=0, padx=0, pady=0)
# SINGLEPLAYER button
b[1] = Button(frame1,
              text='SINGLEPLAYER\nGAME',
              command=lambda: showXOGrid(1, frame1, headerTxt),
              background=c_black,
              bd=0,
              font=('Agency FB', 15),
              foreground=c_aqua1,
              width=30,
              activebackground=c_aqua1,
              activeforeground=c_black,
              cursor="hand2")
b[1].grid(row=1, column=1, padx=0, pady=0)
# empty button for spacing
b[2] = Button(frame1,
              text='\n',
              background=c_black,
              bd=0,
              font=('Agency FB', 15),
              foreground=c_aqua1,
              width=5,
              activebackground=c_black)
b[2].grid(row=1, column=2, padx=0, pady=0)
# MULTIPLAYER button
b[3] = Button(frame1,
              text='MULTIPLAYER\nGAME',
              command=lambda: showXOGrid(2, frame1, headerTxt),
              background=c_black,
              bd=0,
              font=('Agency FB', 15),
              foreground=c_aqua1,
              width=30,
              activebackground=c_aqua1,
              activeforeground=c_black,
              cursor="hand2")
b[3].grid(row=1, column=3, padx=0, pady=0)
# empty button for spacing
b[4] = Button(frame1,
              text='\n',
              background=c_black,
              bd=0,
              font=('Agency FB', 15),
              foreground=c_aqua1,
              width=5,
              activebackground=c_black)
b[4].grid(row=1, column=4, padx=0, pady=0)

# text
# welcomeTxt = Label(frame1,text='MULTIPLAYER GAME',foreground=c_white,background=c_black,font=('Agency FB',25))
# welcomeTxt.grid(row=0,column=0,columnspan=3,padx=20,pady=20)

# #buttons
# b=[0 for x in range(0,10)]
# b[1] = Button(frame2,command=lambda: displaySelection(1),background=c_black,relief=FLAT,bd=0,font=('Agency FB',45),foreground=c_aqua1,width=4,text="   ",activebackground=c_black)
# b[1].grid(row=1,column=0,padx=0,pady=0)
# b[2] = Button(frame2,command=lambda: displaySelection(2), background=c_black,relief=FLAT,bd=0,font=('Agency FB',45),foreground=c_aqua1,width=4,text="   ",activebackground=c_black)
# b[2].grid(row=1,column=1,padx=2,pady=0)
# b[3] = Button(frame2,command=lambda: displaySelection(3), background=c_black,relief=FLAT,bd=0,font=('Agency FB',45),foreground=c_aqua1,width=4,text="   ",activebackground=c_black)
# b[3].grid(row=1,column=2,padx=0,pady=0)
# b[4] = Button(frame2,command=lambda: displaySelection(4), background=c_black,relief=FLAT,bd=0,font=('Agency FB',45),foreground=c_aqua1,width=4,text="   ",activebackground=c_black)
# b[4].grid(row=2,column=0,padx=0,pady=0)
# b[5] = Button(frame2,command=lambda: displaySelection(5), background=c_black,relief=FLAT,bd=0,font=('Agency FB',45),foreground=c_aqua1,width=4,text="   ",activebackground=c_black)
# b[5].grid(row=2,column=1,padx=0,pady=0)
# b[6] = Button(frame2,command=lambda: displaySelection(6), background=c_black,relief=FLAT,bd=0,font=('Agency FB',45),foreground=c_aqua1,width=4,text="   ",activebackground=c_black)
# b[6].grid(row=2,column=2,padx=0,pady=2)
# b[7] = Button(frame2,command=lambda: displaySelection(7), background=c_black,relief=FLAT,bd=0,font=('Agency FB',45),foreground=c_aqua1,width=4,text="   ",activebackground=c_black)
# b[7].grid(row=3,column=0,padx=0,pady=0)
# b[8] = Button(frame2,command=lambda: displaySelection(8), background=c_black,relief=FLAT,bd=0,font=('Agency FB',45),foreground=c_aqua1,width=4,text="   ",activebackground=c_black)
# b[8].grid(row=3,column=1,padx=2,pady=0)
# b[9] = Button(frame2,command=lambda: displaySelection(9), background=c_black,relief=FLAT,bd=0,font=('Agency FB',45),foreground=c_aqua1,width=4,text="   ",activebackground=c_black)
# b[9].grid(row=3,column=2,padx=0,pady=0)
# quitButton = Button(frame3,command=root.destroy,text="QUIT",width=10,relief=FLAT,bd=0,background=c_black, foreground=c_aqua1,activebackground=c_black,activeforeground=c_black,font=('Agency FB',20))
# quitButton.grid(row=0,column=0,padx=10,pady=0)
# restartButton = Button(frame3,command=restartGame,text="RESTART",width=10,relief=FLAT,bd=0,background=c_black, foreground=c_aqua1,activebackground=c_black,activeforeground=c_black,font=('Agency FB',20))
# restartButton.grid(row=0,column=1,padx=10,pady=0)

# variables

x = 1
o = -1
currentPlayer = x
TTTArray = np.zeros(shape=[3, 3])

root.mainloop()
