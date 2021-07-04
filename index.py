#imports
import random
#imports

#code
randNum = random.randint(0, 101)

def checkNumber( input ):
    if input == randNum:
        print("Yay You Have Guessed the Number!")
        return True
    elif input > randNum:
        print("your Number is Too High")
        return False
    elif input < randNum:
        print("Your Number is Too Low!")
        return False
    else:
        print("Please Enter Number")
        return False

def getGuess():
    return int(input( "Enter your guess here: "))

query = getGuess()
result = checkNumber(query)
if result:
    print("")
else:
    query = getGuess()
    result = checkNumber(query)
    if result:
        print("")
    else:
        query = getGuess()
        result = checkNumber(query)
        if result:
            print("")
        else:
            query = getGuess()
            result = checkNumber(query)
            if result:
                print("")
            else:
                query = getGuess()
                result = checkNumber(query)
                print(randNum)

#code
