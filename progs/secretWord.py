secretWord = 'chupacabra'
counter = 0

while True:
    userInput = input('Enter a word: ')
    if userInput == secretWord:
        break
    counter += 1

print('You\'ve successfully left the loop and you guessed: ', counter, 'times')
