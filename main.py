import random
from random import randint

operator_list = ['+', '-', '*', '/']
complexity = ['easy', 'medium', 'hard']

# game logic
def game(points, operators_list, num1, num2):
    # variable to count player score
    count = 1
    print("Solve as quick as possible")
    while count <= 5:
        # Generating unique numbers
        num1, num2 = (random.randint(1, 100), random.randint(1, 100))
        print(f"Q{count}’s out")
        # Generating a random operator every time
        operator_selector = random.choice(operators_list)
        if operator_selector == '+':
            count += 1
            result = num1 + num2
            print(f'{num1} {operator_selector} {num2} = ', end=' ')
            player_input = int(input())
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
            player_input = int(input())
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
            player_input = int(input())
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

    print('===============================')
    print('Welcome to the PUZZLE world!')
    print('===============================')
    print("""\tChoose complexity
            1. Easy
            2. Medium
            3. Hard""")

    # variable to store point for the variable
    score = 0
    complexity_choice = int(input('Choose complexity from the above : '))

    print("-- Let's see how quick you are! --")
    if complexity_choice == 1:  # for Easy complexity
        # Generating two numbers at each iteration
        game(score, operator_list, complexity_choice)
        game_again(flag)
    elif complexity_choice == 2:  # for medium complexity
        # Generating two new numbers at each iteration
        number1, number2 = (random.uniform(101, 500), random.uniform(101, 500))
        number1, number2 = round(number1, random.randint(1, 3)), round(number2, random.randint(1, 3))
        game(score, number1, number2, operator_list)
        game_again(flag)
    elif complexity_choice == 3:  # for hard choice
        # Generating two new numbers at each iteration
        number1, number2 = (random.uniform(501, 1000), random.uniform(501, 1000))
        number1, number2 = round(number1, random.randint(1, 5)), round(number2, randint(1, 5))
        game(score, number1, number2, operator_list)
        game_again(flag)
    else:
        print('Enter a valid choice')
