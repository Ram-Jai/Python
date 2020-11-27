# Tic-Tac-Toe Standalone

from random import randint, choice

#board of the game
board = {'1':' ', '2':' ', '3':' ',
         '4':' ', '5':' ', '6':' ',
         '7':' ', '8':' ', '9':' '}


#board picture
def display(board):
    print('\n')
    #print('Enter the number to put your X or O in there')
    print(' ',board['1'],'|',board['2'],'|',board['3'])
    print('-------------')
    print(' ',board['4'],'|',board['5'],'|',board['6'])
    print('-------------')
    print(' ',board['7'],'|',board['8'],'|',board['9'])


#board numeric picture
def numeric_display():  
    print('\n')
    print(' ',1,'|',2,'|',3)
    print('-------------')
    print(' ',4,'|',5,'|',6)
    print('-------------')
    print(' ',7,'|',8,'|',9)


def winner(board):
    flag = 0
    
    if (board['1']==board['2']==board['3']!=' '):
        flag = 1
    elif (board['4']==board['5']==board['6']!=' '):
        flag = 1
    elif (board['7']==board['8']==board['9']!=' '):
        flag = 1
    elif (board['1']==board['4']==board['7']!=' '):
        flag = 1
    elif (board['2']==board['5']==board['8']!=' '):
        flag = 1
    elif (board['3']==board['6']==board['9']!=' '):
        flag = 1
    elif (board['1']==board['5']==board['9']!=' '):
        flag = 1
    elif (board['3']==board['5']==board['7']!=' '):
        flag = 1
    
    return flag


def single_player_mode(board):
    
    node = input("Player, what's your choice? 'x' or 'o':    ")
    if node == 'x':
        print("Player: x\tComputer: o")
    else:
        print("Player: o\tComputer: x")
    
    
    for i in range(9):
        while True:
            numeric_display()
            print('Enter the number to put your X or O in there')
            display(board)
            turn = input('Your turn...!')
            
            if board[turn] == ' ':
                board[turn] = node
                break
            else:
                print('Wrong move!!!')
                numeric_display()
                print('Enter the number to put your X or O in there')
                display(board)
                turn = input()
        
        check = winner(board)
        
        if check == 1:
            print("The winner is ", node)
            break
        else:
            print('Continue the game...')
                
        if node == 'x':
            node = 'o'
            
        else:
            node = 'x'
         
        while True:  
            computer = str(randint(1, 9))
            print("Computer's turn...!")
            turn = computer
            
            if board[turn] == ' ':
                board[turn] = node
                break
            else:
                print('Wrong move!!!')
                numeric_display()
                print('Enter the number to put your X or O in there')
                display(board)
        
        check = winner(board)
        
        if check == 1:
            print("The winner is ", node)
            break
        else:
            print('Continue the game...')
            
        if node == 'x':
            node = 'o'
            
        else:
            node = 'x'
    
    if check == 0:
        print('!!!Match drawn!!!')
            

def two_player_mode(board):
    
    node = input('Player 1, select your choice: ')
    if node == 'x':
        print("Player 1: x\tPlayer 2: o")
    else:
        print("Player 1: o\tPlayer 2: x")
        
    numeric_display()
    print('Enter the number to put your X or O in there')
    
    for i in range(9):
        display(board)
        print('\n')
        turn = input('Your turn...:   ')
        
        while True:
            if board[turn] == ' ':
                board[turn] = node
                break
            else:
                print('Wrong move!!!')
                numeric_display()
                print('Enter the number to put your X or O in there')
                display(board)
                turn = input()
        
        check = winner(board)
        
        if check == 1:
            print("The winner is ", node)
            break
        else:
            print('Continue the game...')
        
        if node == 'x':
            node = 'o'
            
        else:
            node = 'x'
            
    if check == 0:
        print("!!!Match draw!!!")
            

def automatic_mode(board):
    
    node = choice(['x', 'o'])
    if node == 'x':
        print("Computer 1: x\tComputer 2: o")
    else:
        print("Computer 1: o\tComputer 2: x")
    
    for i in range(9):
        while True:  
            computer_1 = str(randint(1, 9))
            print("Computer_1 turn...!")
            turn = computer_1
            
            if board[turn] == ' ':
                board[turn] = node
                break
            else:
                print('Wrong move!!!')
                numeric_display()
                print('Enter the number to put your X or O in there')
                display(board)
        
        check = winner(board)
        
        if check == 1:
            print("The winner is ", node)
            break
        else:
            print('Continue the game...')
            
        if node == 'x':
            node = 'o'
            
        else:
            node = 'x'
         
        while True:  
            computer_2 = str(randint(1, 9))
            print("Computer_2 turn...!")
            turn = computer_2
            
            if board[turn] == ' ':
                board[turn] = node
                break
            else:
                print('Wrong move!!!')
                numeric_display()
                print('Enter the number to put your X or O in there')
                display(board)
        
        check = winner(board)
        
        if check == 1:
            print("The winner is ", node)
            break
        else:
            print('Continue the game...')
            
        if node == 'x':
            node = 'o'
            
        else:
            node = 'x'
            
    if check == 0:
        print("\n\n!!!Match draw!!!\n\n")
    
       
    
    
print('*******Welcome to Tic-Tac-Toe*******')
print('Choose your option:')
option = int(input('1. Single-Player Mode\n2. Two-Player Mode\n3. Automatic Mode\n\n'))

if option == 1:
    single_player_mode(board)
    display(board)
    
elif option == 2:
    two_player_mode(board)
    print('\n')
    display(board)

elif option == 3:
    automatic_mode(board)
    display(board)
    
else:
    print('Terminating the game')
