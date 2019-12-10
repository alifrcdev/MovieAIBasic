def getStringWithOptions(prompt, options, minLength=1):
    while True:
        string = input(prompt)
        if len(string) < minLength:
            print("Your answer must be longer than " + str(minLength) + " characters long.")
        elif not string in options:
            print("Type only " + ", ".join(options) + ".")
        else:
            return string


def getString(prompt, minLength=1):
    while True:
        string = input(prompt)
        if len(string) < minLength:
            print("Your answer must be longer than " + str(minLength) + " characters long.")
        else:
            return string


def getSafeInt(prompt):
    while True:
        numberStr = getString(prompt)
        try:
            number = int(numberStr)
        except ValueError:
            print("You must enter a number.")
            continue
        return number


def getSafeIntWithRange(prompt, min, max):
    while True:
        number = getSafeInt(prompt)
        if number > max:
            print("Number should be smaller than " + str(max))
        elif number < min:
            print("Number should be greater than " + str(min))
        else:
            return number
