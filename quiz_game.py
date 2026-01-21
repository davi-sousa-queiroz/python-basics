#Work in Progress.
print("Welcome to the Python Quiz! 🐍")
game_start = input('Press ENTER / RETURN to start.')
name = input("Hello! What is your name?")
name = name.capitalize()
difficulty = input("Select difficulty: (1) Easy 😇, (2) Medium 😅, (3) Hard 😰.")
print(f'Alright {name}, Let\'s test your Python skills 😏')
print(f'Difficulty {difficulty}, here we go!!')
score = 0
if difficulty == '1':
    print('Question 1 😄')
    print('What will this print?')
    print('print(5 + 3 * 2)')
    print('1. 16')
    print('2. 11')
    print('3. 10')
    answerA1 = input('Type your selected answer: 1, 2, or 3.')
    if answerA1 == '2':
        print('Well done.')
        score += 1
        print(f'Your current score is: {score}')
    elif answerA1 == '1':
        print('Oops, that\'s wrong.')
        print(f'Your current score is: {score}')
    elif answerA1 == '3':
        print('Oops, that\'s wrong.')
        print(f'Your current score is: {score}')





