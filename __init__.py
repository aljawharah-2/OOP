theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }


            
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    

                    
Role='X'
count=0

for i in range(9):
      
                
    printBoard(theBoard)
    inp=input(Role + " Role, choose a place for "+ Role + "\n")
    

            
    if theBoard[inp]==' ':
        theBoard[inp] = Role
        count=count+1
        
    
    else:
        print('This place is already exists')
        continue
                                   
# Now we will check if player X or O has won,for every move after 5 moves. 
 
    if count>=5:
    
        if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
            printBoard(theBoard)
            print("\nGame Over.\n")                
            print(" **** " +Role + " won. ****")    
            break


        elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")                
            print(" **** " +Role + " won. ****")
            break
            
            
        elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")                
            print(" **** " +Role + " won. ****")
            break
            
            
        elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")                
            print(" **** " +Role + " won. ****")
            break
       
    
        elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")                
            print(" **** " +Role + " won. ****")
            break
            
            
        elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")                
            print(" **** " +Role + " won. ****")
            break
            
         
        elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")                
            print(" **** " +Role + " won. ****")
            break
            
        
        elif theBoard['3'] == theBoard['5'] == theBoard['7'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")                
            print(" **** " +Role + " won. ****")
            break
               
    if count==9:
        printBoard(theBoard)
        print("\nGame Over.\n")
        print("Tie")

        
                
    if Role =='X':
       Role = 'O'
    else:
       Role = 'X'     

    

   

