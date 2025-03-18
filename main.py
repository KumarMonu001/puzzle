import random
from random import randint

operator_list = ['+', '-', '*', '/']
complexity = ['easy', 'medium', 'hard']

# game logic
def game(points, operators_list, choice):
    # variable to count player score
    count = 1
    print("Solve as quick as possible")
    while count <= 5:
        # generating unique numbers for different complexity
        if choice == 1:
            num1, num2 = (random.randint(1, 100), random.randint(1, 100))
        elif choice == 2:
            num1, num2 = (random.uniform(101, 500), random.uniform(101, 500))
            num1, num2 = (round(num1, random.randint(1, 2)), round(num2, random.randint(1, 2)))
        else:
             num1, num2 = (random.uniform(501, 1000), random.uniform(501, 1000))
             num1, num2 = (round(num1, random.randint(2, 4)), round(num2, random.randint(2, 4)))
        print(f"Q{count}’s out")
        # Generating a random operator every time
        operator_selector = random.choice(operators_list)
        if operator_selector == '+':
            count += 1
            result = num1 + num2
            print(f'{num1} {operator_selector} {num2} = ', end=' ')
            player_input = float(input())
            if result == player_input:
                points += 1
                print('WoW : +1')
            else:
                points -= 1
                print('What a Blunder : -1')
        elif operator_selector == '-':
            count += 1
            result = num1 - num2
            print(f'{num1} {operator_selector} {num2} = ', end=' ')
            player_input = float(input())
            if result == player_input:
                points += 1
                print('WoW : +1')
            else:
                points -= 1
                print('What a Blunder : -1')
        elif operator_selector == '*':
            count += 1
            result = num1 * num2
            print(f'{num1} {operator_selector} {num2} = ', end=' ')
            player_input = float(input())
            if result == player_input:
                points += 1
                print('WoW : +1')
            else:
                points -= 1
                print('What a Blunder : -1')
        else:
            count += 1
            result = float(num1) / float(num2)
            print(f'{num1} {operator_selector} {num2} = ', end=' ')
            player_input = float(input())
            if result == player_input:
                points += 1
                print('WoW : +1')
            else:
                points -= 1
                print('What a Blunder : -1')
    print(f'Total points obtained : {points}')


def game_again(flag):
    print("""
        ===== For playing again =====
        ---------- Press 1 ----------
        ====== For Leaving game =====
        ---------- Press 2 ----------
        """)


    choice = int(input('Enter here 1 / 2 : '))

    if choice == 1:
        flag = True
        return flag
    elif choice == 2:
        flag = False
        return flag
    else:
        print('Enter a valid choice!')




# flag -> to decide whether player wants more game or not
flag = True
# Main loop to keep player in the
while flag:

    print('\n \t===============================')
    print('\tWelcome to the PUZZLE world!')
    print('\t===============================')
    print('''
          Game Instruction:
          -> For complexity - medium - use only 1 digit after point
          -> For complexity - hard - use only 2 digit after point
          ''')
    print("""\tChoose complexity
            1. Easy
            2. Medium
            3. Hard""")

    # variable to store point for the variable
    score = 0
    complexity_choice = int(input('Choose complexity from the above : '))

    print("-- Let's see how quick you are! --")
    if complexity_choice == 1:  # for Easy complexity
        game(score, complexity_choice, operator_list)
        game_again(flag)
    elif complexity_choice == 2:  # for medium complexity
        game(score, complexity_choice, operator_list)
        game_again(flag)
    elif complexity_choice == 3:  # for hard choice
        game(score, complexity_choice, operator_list)
        game_again(flag)
    else:
        print('Enter a valid choice')
