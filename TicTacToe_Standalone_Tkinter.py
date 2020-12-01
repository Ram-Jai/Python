# Tic-Tao-Toe Stadalone game using Tkinter - 2 Player Mode
from tkinter import *
from tkinter.messagebox import showinfo
import warnings

#Removes all the warning from the output
warnings.filterwarnings('ignore')

root=Tk()


numbers=[1,2,3,4,5,6,7,8,9] 
# y='X' for player1 and 'O' for player2
y=""
# x is the counter to keep counting the number of chances
x=0
#boards is a list to store the mark with respect to the cell number

board = {1:' ', 2:' ', 3:' ',
         4:' ', 5:' ', 6:' ',
         7:' ', 8:' ', 9:' '}

def result(board,mark):
    return ((board[1] == board[2] == board[3] == mark) 
            or (board[4] == board[5] == board[6] == mark) 
            or (board[7] == board[8] == board[9] == mark) 
            or (board[1] == board[4] == board[7] == mark) 
            or (board[2] == board[5] == board[8] == mark)
            or (board[3] == board[6] == board[9] == mark)
            or (board[1] == board[5] == board[9] == mark) 
            or (board[3] == board[5] == board[7] == mark))


def define_sign(number):
    global x,y,numbers
    """ Checking which button has been clicked and checking if the button has been already clicked or not to avoid over-writing"""
    for i in range(1,10):
        if number==i and number in numbers:
            numbers.remove(number)
           
            # If the value of x is even, Person1 will play and vivee versa
            if x%2==0:
                y='X'
                board[number]=y
            elif x%2!=0:
                y='O'
                board[number]=y
            #Using config, we write mark the button with appropriate value. 
            b[i].config(text=y)
            x=x+1
            mark=y
            # Here we are calling the result() to decide whether we have got the winner or not
            if(result(board,mark) and mark=='X' ):
                #If Player1 is the winner show a dialog box stating the winner
                showinfo("Result","Player1 wins")
                #Call the destroy function to close the GUI
                destroys()
            elif(result(board,mark) and mark=='O'):
                showinfo("Result","Player2 wins")
                destroys()

            
    # If we have not got any winner, display the dialogbox stating the match has bee tied.
    if(x>8 and result(board,'X')==False and result(board,'O')==False):
        showinfo("Result","Match Tied")
        destroys()
        


label1=Label(root,text="Player 1 : X",font="times 18")
label1.grid(row=0,column=1)


l2=Label(root,text="Player 2 : O",font="times 18")
l2.grid(row=0,column=2)


def destroys():
    # destroys the window when called
    root.destroy()

b = [i for i in range(10)]
    
b[1]=Button(root,font='normal 50 normal', bg='white', fg='black',width=5,height=3,command=lambda :define_sign(1))
b[1].grid(row=1,column=1)
b[2]=Button(root,font='normal 50 normal', bg='white', fg='black',width=5,height=3,command=lambda: define_sign(2))
b[2].grid(row=1,column=2)
b[3]=Button(root,font='normal 50 normal', bg='white', fg='black',width=5,height=3,command=lambda: define_sign(3))
b[3].grid(row=1,column=3)
b[4]=Button(root,font='normal 50 normal', bg='white', fg='black',width=5,height=3,command=lambda: define_sign(4))
b[4].grid(row=2,column=1)
b[5]=Button(root,font='normal 50 normal', bg='white', fg='black',width=5,height=3,command=lambda: define_sign(5))
b[5].grid(row=2,column=2)
b[6]=Button(root,font='normal 50 normal', bg='white', fg='black',width=5,height=3,command=lambda: define_sign(6))
b[6].grid(row=2,column=3)
b[7]=Button(root,font='normal 50 normal', bg='white', fg='black',width=5,height=3,command=lambda: define_sign(7))
b[7].grid(row=3,column=1)
b[8]=Button(root,font='normal 50 normal', bg='white', fg='black',width=5,height=3,command=lambda: define_sign(8))
b[8].grid(row=3,column=2)
b[9]=Button(root,font='normal 50 normal', bg='white', fg='black',width=5,height=3,command=lambda: define_sign(9))
b[9].grid(row=3,column=3)
root.mainloop()
