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