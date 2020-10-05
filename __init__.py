theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }
            
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    
 
printBoard(theBoard)

Role='X'
count=0

for i in range(10):

    inp=input(Role + " Role, choose a place for "+ Role + "\n")
    if theBoard[inp]==' ':
     theBoard[inp] =Role
     printBoard(theBoard)
     count=+1
    else:
     print('This place is already exists')
     continue
        
    if Role =='X':
       Role = 'O'
    else:
       Role = 'X'     


   

