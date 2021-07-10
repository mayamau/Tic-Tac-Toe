# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 23:52:33 2018

@author: maya
"""

#import
from tkinter import *
import tkinter.messagebox
from random import randint
import time
import numpy as np
#create root window
root=Tk()
#modify root window
root.title("Tic Tac Toe")
root.configure(background="#030305")

#functions
def restartGame():
    global x
    global o
    global TTTArray
    global disable
    global filled
    TTTArray.fill(0)
    for s in range(1,10):
        b[s].config(state=NORMAL,text=' ') 
        x=1
        o=-1 
        disable=False
        filled=False
    
def popupfunc(resultString):

    pop = Toplevel(root)
    pop.title("Result")
    frame0 = Frame(pop,bg="#030305",bd=0,relief=FLAT) 
    frame0.pack()
    
    resultTxt = Label(frame0,text=resultString,foreground='#FFFFFF',background="#030305",font=('Agency FB',20))     
    resultTxt.grid(row=0,column=0,padx=20,pady=20) 
    
    okButton = Button(frame0,command=pop.destroy,text="OK",width=10,relief=FLAT,bd=0,background='#030305', foreground='#91FCFF',activebackground='#030305',activeforeground='#030305',font=('Agency FB',20))
    okButton.grid(row=1,column=0,padx=10,pady=0)
    
    for s in range(1,10):
        b[s].config(state=DISABLED,disabledforeground='#91FCFF')
    
def displaySelection(val):
    global x
    global o
    global TTTArray
    global disable
    global filled
    global resultString
    dict={1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2]}
    pos=[]
    for i in dict:
        if i==val:
            pos=dict[val]
            i=pos[0]
            j=pos[1]
            if TTTArray[i,j]==0:
                if x==1 and o==-1:
                   TTTArray[i,j]=100
                   b[val].config(text="X")
                   x=-1
                   o=1
                else:
                    TTTArray[i,j]=200
                    b[val].config(text="O")
                    x=1
                    o=-1
    c=0
    for r in range(0,3):
        if((TTTArray[r,c]==TTTArray[r,c+1]==TTTArray[r,c+2]==200) or (TTTArray[r,c]==TTTArray[r,c+1]==TTTArray[r,c+2]==100)):
            if (TTTArray[r,c]==200):
                resultString="O wins!"
            else:
                resultString="X wins!"
            disable=True 
            
        
            
    r=0
    for c in range(0,3):
        if((TTTArray[r,c]==TTTArray[r+1,c]==TTTArray[r+2,c]==200) or(TTTArray[r,c]==TTTArray[r+1,c]==TTTArray[r+2,c]==100)) :
            if (TTTArray[r,c]==200):
                resultString="O wins!"
            else:
                resultString="X wins!"
            disable=True
    r=1
    c=1
    if(((TTTArray[r,c]==TTTArray[r-1,c+1]==TTTArray[r+1,c-1]==100) or (TTTArray[r,c]==TTTArray[r+1,c+1]==TTTArray[r-1,c-1]==100)) or ((TTTArray[r,c]==TTTArray[r-1,c+1]==TTTArray[r+1,c-1]==200) or (TTTArray[r,c]==TTTArray[r+1,c+1]==TTTArray[r-1,c-1]==200))):
        if (TTTArray[r,c]==200):
            resultString="O wins!"
        else:
            resultString="X wins!"
        disable=True       
                
    if(disable==True):
        popupfunc(resultString)
        for s in range(0,3):
            for t in range(0,3):
                TTTArray[s,t]=999
    else:
        filled=True
        for s in range(0,3):
            for t in range(0,3):
                if (TTTArray[s,t]==0):
                    filled=False
        if filled==True:
            popupfunc("Its a draw!")
 
#frame
frame1 = Frame(root,bg="#030305",bd=0,relief=FLAT) 
frame1.pack(padx=0,pady=0) 
frame2 = Frame(root, bg="#00E7ED",bd=0,relief=FLAT) 
frame2.pack(padx=70,pady=0)  
frame3 = Frame(root, bg="#030305",bd=0,relief=FLAT) 
frame3.pack(padx=0,pady=30)
       
#text
welcomeTxt = Label(frame1,text='MULTIPLAYER GAME',foreground='#FFFFFF',background="#030305",font=('Agency FB',25))     
welcomeTxt.grid(row=0,column=0,columnspan=3,padx=20,pady=20)    
   
#buttons
b=[0 for x in range(0,10)] 
b[1] = Button(frame2,command=lambda: displaySelection(1),background='#030305',relief=FLAT,bd=0,font=('Agency FB',45),foreground='#91FCFF',width=4,text="   ",activebackground='#030305')
b[1].grid(row=1,column=0,padx=0,pady=0)
b[2] = Button(frame2,command=lambda: displaySelection(2), background='#030305',relief=FLAT,bd=0,font=('Agency FB',45),foreground='#91FCFF',width=4,text="   ",activebackground='#030305')
b[2].grid(row=1,column=1,padx=2,pady=0)
b[3] = Button(frame2,command=lambda: displaySelection(3), background='#030305',relief=FLAT,bd=0,font=('Agency FB',45),foreground='#91FCFF',width=4,text="   ",activebackground='#030305')
b[3].grid(row=1,column=2,padx=0,pady=0)
b[4] = Button(frame2,command=lambda: displaySelection(4), background='#030305',relief=FLAT,bd=0,font=('Agency FB',45),foreground='#91FCFF',width=4,text="   ",activebackground='#030305')
b[4].grid(row=2,column=0,padx=0,pady=0)
b[5] = Button(frame2,command=lambda: displaySelection(5), background='#030305',relief=FLAT,bd=0,font=('Agency FB',45),foreground='#91FCFF',width=4,text="   ",activebackground='#030305')
b[5].grid(row=2,column=1,padx=0,pady=0)
b[6] = Button(frame2,command=lambda: displaySelection(6), background='#030305',relief=FLAT,bd=0,font=('Agency FB',45),foreground='#91FCFF',width=4,text="   ",activebackground='#030305')
b[6].grid(row=2,column=2,padx=0,pady=2)
b[7] = Button(frame2,command=lambda: displaySelection(7), background='#030305',relief=FLAT,bd=0,font=('Agency FB',45),foreground='#91FCFF',width=4,text="   ",activebackground='#030305')
b[7].grid(row=3,column=0,padx=0,pady=0)
b[8] = Button(frame2,command=lambda: displaySelection(8), background='#030305',relief=FLAT,bd=0,font=('Agency FB',45),foreground='#91FCFF',width=4,text="   ",activebackground='#030305')
b[8].grid(row=3,column=1,padx=2,pady=0)
b[9] = Button(frame2,command=lambda: displaySelection(9), background='#030305',relief=FLAT,bd=0,font=('Agency FB',45),foreground='#91FCFF',width=4,text="   ",activebackground='#030305')
b[9].grid(row=3,column=2,padx=0,pady=0)
quitButton = Button(frame3,command=root.destroy,text="QUIT",width=10,relief=FLAT,bd=0,background='#030305', foreground='#91FCFF',activebackground='#030305',activeforeground='#030305',font=('Agency FB',20))
quitButton.grid(row=0,column=0,padx=10,pady=0)
restartButton = Button(frame3,command=restartGame,text="RESTART",width=10,relief=FLAT,bd=0,background='#030305', foreground='#91FCFF',activebackground='#030305',activeforeground='#030305',font=('Agency FB',20))
restartButton.grid(row=0,column=1,padx=10,pady=0)

#variables
x=1
o=-1 
disable=False
filled=False
TTTArray=np.zeros(shape=[3,3])
        
root.mainloop() 
