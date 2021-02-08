from random import randint
import math

# 1) Write a function that emulates the game "rock, scissors, paper"
# At the entrance, your function accepts your version printed from the console, the computer makes a decision randomly.


def game_rsp(player):
    choice = {1: 'Rock',
              2: 'SCISSORS',
              3: 'PAPER'
              }
    computer = randint(1, 3)
    win = ''
    if computer == player:
        win = 'DRAW'
    if player == 1 and computer == 2:
        win = 'player'
    if player == 1 and computer == 3:
        win = 'computer'
    if player == 2 and computer == 1:
        win = 'computer'
    if player == 2 and computer == 3:
        win = 'player'
    if player == 3 and computer == 1:
        win = 'player'
    if player == 3 and computer == 2:
        win = 'computer'
    print(f'player entered {choice.get(player)}\ncomputer choice {choice.get(computer)}\nwin {win}')


player_ = int(input('Entered 1 = ROCK 2 = SCISSORS 3 = PAPER: '))
game_rsp(player_)

# 2)Try to imagine a world in which you might have to stay home for (Corona virus) 14 days at any given time.
# Do you have enough toilet paper(TP) to make it through?
# Although the number of squares per roll of TP varies significantly, we'll assume each roll has 500 sheets,
# and the average person uses 57 sheets per day.

# Create a function that will receive a dictionary with two key/values:
# "people" ⁠— Number of people in the household.
# "tp" ⁠— Number of rolls.
# Return a statement telling the user if they need to buy more TP!


def count_rolls(people=1, tp=0):
    need_rolls = math.ceil(people*57*14/500)
    if need_rolls <= tp:
        print('You have enough toilet paper')
    else:
        to_buy = need_rolls - tp
        print(f'You need to buy {to_buy} rolls')


dictionary = {
    "people": 3,
    "tp": 1
}


def count_rolls1(dict_):
    need_rolls = math.ceil(dict_.get('people')*57*14/500)
    if need_rolls <= dict_.get('tp'):
        print('You have enough toilet paper')
    else:
        to_buy = need_rolls - dict_.get('tp')
        print(f'You need to buy {to_buy} rolls')


count_rolls(3, 1)
count_rolls1(dictionary)


# 3) Make a function that encrypts a given input with these steps:
# Input: "apple"
# Step 1: Reverse the input: "elppa"
# Step 2: Replace all vowels using the following chart:
# a => 0
# e => 1
# i => 2
# o => 2
# u => 3
# # "1lpp0"
# Example:
# encrypt("banana") ➞ "0n0n0baca"
# encrypt("karaca") ➞ "0c0r0kaca"
# encrypt("burak") ➞ "k0r3baca"
# encrypt("alpaca") ➞ "0c0pl0aca"


def encrypt(line):
    charts = {
        'a': 0,
        'e': 1,
        'i': 2,
        'o': 2,
        'u': 3
    }
    line = line[::-1]
    result = ''
    for ch in line:
        if ch in charts.keys():
            result += str(charts[ch])
        else:
            result += ch
    return result


print(encrypt(input('Entered line: ')))


# **4)Given a 3x3 matrix of a completed tic-tac-toe game, create a function that returns whether the game is a win
# for "X", "O", or a "Draw", where "X" and "O" represent themselves on the matrix, and "E" represents an empty spot.
# Example:

tic_tac_toe = ([
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", "X", "X"]]) #➞ "X"
#
tic_tac_toe1 =([
    ["O", "O", "O"],
    ["O", "X", "X"],
    ["E", "X", "X"]
 ]) #➞ "O"
#

tic_tac_toe2 = ([
    ["X", "X", "0"],
    ["0", "O", "X"],
    ["X", "X", "O"]])
# ➞ "Draw"


def is_win(array):

    def horizontal():
        for i in range(len(array)):
            w = array[i][0]
            win = 'Draw'
            for j in range(len(array)):

                if array[i][j] == w and array[i][j] != 'E':
                    win = array[i][0]
                    continue
                else:
                    win = 'Draw'
                    break
            return win

    def vertical():
        for i in range(len(array)):
            w = array[i][0]
            win = 'Draw'
            for j in range(len(array)):

                if array[j][i] == w and array[j][i] != 'E':

                    win = array[j][i]
                    continue
                else:
                    win = 'Draw'
                    break
            return win

    def diagonal():
        win = 'Draw'
        for x in range(len(array)):
            w = array[0][0]
            if array[x][x] == w and array[x][x] != 'E':
                win = array[x][x]
                continue
            else:
                win = 'Draw'
                break

        if win == 'Draw':
            for i in range(len(array)):
                y = len(array) - 1 - i
                w = array[i][len(array) - 1]
                if array[i][y] == w and array[i][y] != 'E':
                    win = array[i][y]
                    continue
                else:
                    win = 'Draw'
                    break
        return win

    if horizontal() != 'Draw':
        winner = horizontal()
    elif vertical() != 'Draw':
        winner = vertical()
    elif diagonal() != 'Draw':
        winner = diagonal()
    else:
        winner = 'draw'

    print(winner)


is_win(tic_tac_toe)
is_win(tic_tac_toe1)
is_win(tic_tac_toe2)