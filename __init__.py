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

    X=input("X Role, choose a place for X\n")
    if theBoard[X]==' ':
     theBoard[X] ='X'
     printBoard(theBoard)
    else:
     print('This place is already exists')
