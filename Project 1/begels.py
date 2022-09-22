import random

NUM_DIGITS = 3
NUM_GUESS = 10

def main():

    while True:
        # Store secret number that player needs to guess
        # .format putting any object inside the square bracket
        secretNum = generateNumber()
        print('I have a number..')
        print('You have {} chance to guess the correct number'.format(NUM_GUESS))

        countGuesses = 0 

        while countGuesses < NUM_GUESS:
            guess = ''
            
            # checker, players need to inputs correct answer's format
            # isnumeric check whether the string is a number or not

            if len(guess) != NUM_DIGITS or not guess.isnumeric():
                print('This is your #{} guess'.format(countGuesses+1))
                guess = input('> ')

            
            if guess == secretNum:
                # the guess is correct
                print('Your guess is correct!')
                break

            # generate the clues from the clues() function
            clues = generateClues(guess, secretNum)
            print(clues)
            countGuesses+=1

            if countGuesses > NUM_GUESS:
                print('You run out of guesses')
                print('The answer is {}, good luck later'.format(secretNum))

        print('Do you want play again (yes or no)?')
        if not input('> ').startswith('y'):
            break

        print('Thanks for playing!')

# def generateClue(guess, secretNum):

def generateNumber():

    numbers = list('0123456789')
    random.shuffle(numbers)
    # print(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += numbers[i]

    return secretNum

def generateClues(guess, secretNum):
    # By Al Sweigart al@inventwithpython.com

    # I am thinking of a {}-digit number with no repeated digits.
    # Try to guess what it is. Here are some clues:
    # When I say:    That means:
    #   Pico         One digit is correct but in the wrong position.
    #   Fermi        One digit is correct and in the right position.
    #   Bagels       No digit is correct.

    # For example, if the secret number was 248 and your guess was 843, the
    # clues would be Fermi Pico.

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')

        elif guess[i] in secretNum:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Begels'

    else:
        clues.sort()
        # return the clues using alphabetical order so we are not giving too much information.

        return ' '.join(clues) 

if __name__ == '__main__':
    main()

# Program Exploration

# 1. What happens when you change the NUM_DIGITS constant?
# 2. What happens when you change the MAX_GUESSES constant?
# 3. What happens if you set NUM_DIGITS to a number larger than 10?
# If we change the number of digits to > 10 It will be error because the list of numbers only 10.
# 4. What happens if you replace secretNum = getSecretNum() on line 30 with secretNum = '123'?
# the secret number will constantly be 123
# 5. What error message do you get if you delete or comment out numGuesses = 1 on line 34?
# It will be error since we need the guess counter
# 6. What happens if you delete or comment out random.shuffle(numbers) on line 62?
# The guess number will only 0,1,2
# 7. What happens if you delete or comment out if guess == secretNum: on line 74 and return 'You got it!' on line 75?
# for any correct or even incorrect answer will be returned "You got it!"
# 8. What happens if you comment out numGuesses += 1 on line 44?
# You will have unlimited chance to guess the number