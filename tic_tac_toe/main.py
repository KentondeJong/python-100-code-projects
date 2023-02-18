import random

characters = ['X', 'O']
user_char = ''
spots = ['', '', '', '', '', '', '', '', '']

def chooseChar():
    global user_char
    user_char = input('What character would you like to use? (X or O) ').upper()
    if user_char in characters:
        characters.remove(user_char)
    else:
        chooseChar()

def readBoard():
    print('')
    print(f"{spots[0]} | {spots[1]} | {spots[2]}")
    print('------')
    print(f"{spots[3]} | {spots[4]} | {spots[5]}")
    print('------')
    print(f"{spots[6]} | {spots[7]} | {spots[8]}")
    print('')

def playerPlays():
    readBoard()
    spot = int(input(f"Where would you like to put your {user_char}? (1-9) ")) - 1

    if spot < 0:
        spot = 0

    if spots[spot] == '':
        spots[spot] = user_char
        if checkGrid(user_char) is False:
            compPlays()
    else:
        print(spot)
        print(spots)
        print(spots[spot])
        print('That spot is taken. Try again.')
        playerPlays()

def checkGrid(char):
    readBoard()
    if (spots[0] == char and spots[1] == char and spots[2] == char):
        print(f"{char} wins!")
        return True
    elif (spots[0] == char and spots[3] == char and spots[6] == char):
        print(f"{char} wins!")
        return True
    elif (spots[0] == char and spots[4] == char and spots[8] == char):
        print(f"{char} wins!")
        return True
    elif (spots[1] == char and spots[4] == char and spots[7] == char):
        print(f"{char} wins!")
        return True
    elif (spots[2] == char and spots[5] == char and spots[8] == char):
        print(f"{char} wins!")
        return True
    elif (spots[2] == char and spots[4] == char and spots[6] == char):
        print(f"{char} wins!")
        return True
    elif (spots[3] == char and spots[4] == char and spots[5] == char):
        print(f"{char} wins!")
        return True
    else:
        return False

def compPlays():
    spot = random.randint(0, len(spots)-1)
    if spots[spot] == '':
        spots[spot] = characters[0]
        if checkGrid(characters[0]) is False:
            playerPlays()
    else:
        compPlays()
    

chooseChar()
playerPlays()
