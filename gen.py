
import random

ALPHA = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
CHARACTERS = [ "!", "£", "$", "%", "^", "&", "*", "(", ")", "[", "]", "{", "}", "#", "@", ":", ";", "/", "?", ">", "<",]
FULL = ALPHA + CHARACTERS


def getpasswordType():
    while True:
        print("passwordType 1 for alphanumeric passwordType 2 for full character set")
        passwordType = input()
        if passwordType == '1':
            return 'alpha'
        elif passwordType == '2':
            return 'full'

def getLength():
    while True:
        print("Choose password length between 10 and 30")
        length = input()
        if int(length) >= 10 and int(length) <= 30:
            return(length)
            break

def generatePassword(passwordType, length):
    result = []
    if passwordType == 'alpha':
        charList = ALPHA
    elif passwordType == 'full':
        charList = FULL
    i = 0
    int(length)
    while i < length:
        randomChoice = random.choice(charList)
        result.append(randomChoice)
        
        i += 1
    password = ''.join(result)
    print(password)


def main():
    while True:
        passwordType = getpasswordType()
        length = getLength()
        intLength = int(length)
        if passwordType == 'alpha':
            password = generatePassword(passwordType, intLength)
        elif passwordType == 'full':
            password = generatePassword(passwordType, intLength)
        print("type end to stop program ot enter to run program again")
        x = input()
        if x == "end":
            exit()

main()