def check_format(val):
    if val=='_':
        return(' ')
    else:
        return(val)

def print_grid(input_text):
    print("---------")
    print("| {} {} {} |".format(check_format(input_text[0]),check_format(input_text[1]),check_format(input_text[2])))
    print("| {} {} {} |".format(check_format(input_text[3]),check_format(input_text[4]),check_format(input_text[5])))
    print("| {} {} {} |".format(check_format(input_text[6]),check_format(input_text[7]),check_format(input_text[8])))
    print("---------")    



def check_win(val):
    win=False
    j=0
    # check rows for a win
    for i in range(0,9,3):
        if input_text[i:i+3]==val*3:
            return(True)
    
    # check columns for a win
    for i in range(3):
        column=''.join([input_text[j] for j in range(i,9,3)])
        if column==val*3:
            return(True)
    # check 1st diagonal for a win
    if ''.join([input_text[i] for i in range(0,9,4) ])==val*3:
        return(True)
    # check 2nd diagonal for a win
    if ''.join([input_text[i] for i in range(2,7,2) ])==val*3:
        return(True)
               
    return(win)

def check_result(input_text):
    # variables
    game_result=""
    did_X_win=False
    did_O_win=False
    is_board_full=False
    num_X=len([input_text[i] for i in range(len(input_text)) if input_text[i]=='X'])
    num_O=len([input_text[i] for i in range(len(input_text)) if input_text[i]=='O'])
    num_null=9-num_X-num_O

    did_X_win=check_win("X")
    did_O_win=check_win("O")

    if num_null==0:
        is_board_full=True

    if abs(num_X-num_O)>1 or (did_X_win and did_O_win) :
        game_result="Impossible"
    elif did_X_win and not did_O_win:
        game_result="X wins"
    elif not did_X_win and did_O_win:
        game_result="O wins"
    elif not is_board_full:
        game_result="Game not finished"
    else:
        game_result="Draw"
    return(game_result)

def get_next_move(input_string,player):
    output_string=""
    while (True):
        input_cells=input("Enter the coordinates:").split(' ')
        try:
            casted_input_cells=[int(i) for i in input_cells]
        except:
            print("You should enter numbers!")
            continue
        if len(list(filter(lambda x: x<1 or x>3,casted_input_cells))):
            print("Coordinates should be from 1 to 3!")
            continue
        index=(casted_input_cells[0]-1)*3+(casted_input_cells[1]-1)
        if input_string[index]!='_':
            print("This cell is occupied! Choose another one!")
            continue
        output_string=input_string[:index]+player+input_string[index+1:]
        break
    return(output_string)
        
            
if __name__=='__main__':
    input_text="_________"
    print_grid(input_text)
    game_result="Game not finished"
    player="X"
    while game_result=="Game not finished":
        input_text=get_next_move(input_text,player)
        print_grid(input_text)
        game_result=check_result(input_text)
        if player=="X":
            player="O"
        else:
            player="X"
    print(game_result)
