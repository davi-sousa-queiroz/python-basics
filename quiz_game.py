#First GitHub Project (January 22nd 2026)
print("Welcome to the Python Quiz! 🐍")
game_start = input('Press ENTER / RETURN to start.')
name = input("Hello! What is your name?")
name = name.capitalize()
difficulty = input("Select difficulty: (1) Easy 😇, (2) Hard 🫣")
print(f'Alright {name}, Let\'s test your Python skills 😏')
print(f'Difficulty {difficulty}, here we go!')
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
    print('Ready for question 2?')
    print('Which of these is the correct way to get input from the user?')
    print('1. input("Enter your name:")')
    print("2. read('Enter your name:')")
    print('3. ask("Enter your name:")')
    answerA2 = input('Type your selected answer: 1, 2, or 3.')
    if answerA2 == '1':
        print('Nice!')
        score += 1
        print(f'Your current score is: {score}')
    elif answerA2 == '2':
        print('Got that one wrong...')
        print(f'Your current score is: {score}')
    elif answerA2 == '3':
        print('Got that one wrong...')
        print(f'Your current score is: {score}')
    print('Last question!')
    print('What data type is the result of 10 / 2 in Python?')
    print('1. int')
    print('2. float')
    print('3. str')
    answerA3 = input('Type your selected answer: 1, 2, or 3.')
    if answerA3 == '2':
        print('Correct, Great Job!')
        score += 1
        print(f'Your current score is: {score}')
    elif answerA3 == '1':
        print('Bad Luck')
        print(f'Your current score is: {score}')
    elif answerA3 == '3':
        print('Bad Luck')
    print('Congrats, You have finished the Python Quiz on easy mode!')
    if score == 0:
        print('Wow.. looks like you got them all wrong.')
        print(f"Your final score was: {score}/3")
    elif score == 1:
        print('Good try.')
        print(f'Your final score was: {score}/3')
    elif score == 2:
        print('Great Job!')
        print(f'Your final score was: {score}/3')
    elif score == 3:
        print('NICE!🔥You Aced the quiz!')
        print(f'Your final score was: {score}/3')
if difficulty == '2':
    print('First Question!')
    print('What will this print?')
    print('x = 7')
    print('y = 3')
    print('print(x // y')
    print('(1) 2.33')
    print('(2) Error')
    print('(3) 2')
    answerB1 = input('Type your selected answer: 1, 2, or 3.')
    if answerB1 == '3':
        print('Correct, Nice!')
        score += 2
        print(f'Your current score is: {score}')
    elif answerB1 == '1':
        print('Nice try!')
        print(f'Your current score is: {score}')
    elif answerB1 == '2':
        print('Incorrect...')
        print(f'Your current score is: {score}')
    print('Second Question!')
    print('What will this print?')
    print('password = "Admin123"')
    print('print(password.isalpha())')
    print('(1) True')
    print('(2) False')
    print('(3)"Admin123"')
    answerB2 = input('Type your selected answer: 1, 2, or 3.')
    if answerB2 == '2':
        print('Correct, Nice!')
        score += 2
        print(f'Your current score is: {score}')
    elif answerB2 == '1':
        print('That is wrong.')
        print(f'Your current score is: {score}')
    elif answerB2 == '3':
        print('That is wrong.')
        print(f'Your current score is: {score}')
    print('FINAL QUESTION!🔥')
    print('What will this print?')
    print('text = "python"')
    print('result = text.upper().replace("P", "J")')
    print('print(result)')
    print('(1) JYTHON')
    print('(2) PYTHON')
    print('(3) jython')
    answerB3 = input('Type your selected answer: 1, 2, or 3.')
    if answerB3 == '1':
        print('Correct, JYTHON!')
        score += 2
    elif answerB3 == '2':
        print('Nope.')
    elif answerB3 == '3':
        print('Nope.')
    if score == 0:
        print('GAME OVER!')
        print('Hard mode was too much this time...')
        print('Train more and come back stronger 💪')
        print(f'Final score: {score}/6')
    elif score == 2:
        print('Somehow.. you survived.')
        print(f'Your final score is: {score}/6')
    elif score == 4:
        print('You completed the quiz ✅')
        print('Nice one! You clearly know python.')
        print(f'Your final score is: {score}/6')
    elif score == 6:
        print('🏆 LEGENDARY SCORE 🏆')
        print('You answered EVERYTHING correctly.')
        print('Feared by python.')
        print(f'Your final score is: {score}/6')


