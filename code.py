game=[(),(),()]*3
def shape():
    print(game[0],game[1],game[2])
    print(game[3],game[4],game[5])
    print(game[6],game[7],game[8])


def X_won():
    return (
       game[0]=='X' and game[1]=='X'and game[2]=='X'
    or game[3]=='X' and game[4]=='X'and game[5]=='X'
    or game[6]=='X' and game[7]=='X'and game[8]=='X'
    or game[0]=='X' and game[3]=='X'and game[6]=='X'
    or game[1]=='X' and game[4]=='X'and game[7]=='X'
    or game[2]=='X' and game[5]=='X'and game[8]=='X'
    or game[0]=='X' and game[4]=='X'and game[8]=='X'
    or game[2]=='X' and game[4]=='X'and game[6]=='X'
    )
    


def O_won():
    return (
       game[0]=='O' and game[1]=='O'and game[2]=='O'
    or game[3]=='O' and game[4]=='O'and game[5]=='O'
    or game[6]=='O' and game[7]=='O'and game[8]=='O'
    or game[0]=='O' and game[3]=='O'and game[6]=='O'
    or game[1]=='O' and game[4]=='O'and game[7]=='O'
    or game[2]=='O' and game[5]=='O'and game[8]=='O'
    or game[0]=='O' and game[4]=='O'and game[8]=='O'
    or game[2]=='O' and game[4]=='O'and game[6]=='O'
    )
    

while True:
    player_X=int(input('X location   '))
    game[player_X]='X'
    shape()
    if X_won():
        print('X player won')
        break
    player_O=int(input('O location   '))
    game[player_O]='O'
    shape()
    if O_won():
        print('O player won')
        break
