num_poss = int(input())
list_poss = []

for _ in range(num_poss):
    list_poss.append(input())

for pos in list_poss:
    convert_int = int(pos, 8);
    convert_bin = format(convert_int, '019b')
    board = []
    for i in range(18):
        if( i < 9 ):
            if( int(convert_bin[18-i]) ):
                board.append('O');
            else:
                board.append('N');
        else:
            if(int(convert_bin[18-i])):
                board[(i%9)] = "X"; 
    start = [0, 1, 2]
    continue_loop = False
    for i in start:
        if((board[(i*3)+start[0]] == board[(i*3)+start[1]] and board[(i*3)+start[1]] == board[(i*3)+start[2]])):
            if(board[(i*3)+start[0]] == "O"):
                print("O wins")
                continue_loop = True
                break
            elif(board[(i*3)+start[0]] == "X"):
                print("X wins")
                continue_loop = True
                break
        elif((board[(start[0]*3)+i] == board[(start[1]*3)+i] and board[(start[1]*3)+i] == board[(start[2]*3)+i])):
            if(board[(start[0]*3)+i] == "O"):
                print("O wins")
                continue_loop = True
                break
            elif(board[(start[0]*3)+i] == "X"):
                print("X wins")
                continue_loop = True
                break
    if( continue_loop):
        continue;
    if(((board[0] == board[4]) and (board[4] == board[8])) or ((board[2] == board[4]) and (board[4] == board[6]))):
        if( board[4] == "O"):
            print("O wins")
            continue
        elif(board[4] == "X"):
            print("X wins")
            continue
    
    if "N" in board:
        print("In progress");
    else:
        print("Cat's");





