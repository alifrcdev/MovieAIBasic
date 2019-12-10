from __future__ import print_function


def printHeadings(headings, maxLens):
    print('|No |', end="")
    for i in range(len(headings)):
        print(' ' + headings[i], end="")
        for a in range(maxLens[i] - len(headings[i])):
            print(' ', end='')
        print(' |', end='')
    print('')


def printRow(pos, names, maxLens):
    print('| ' + str(pos) + ' |', end="")
    for i in range(len(names)):
        print(' ' + names[i], end="")
        for a in range(maxLens[i] - len(names[i])):
            print(' ', end='')
        print(' |', end='')
    print('')


def printTable(title, headings, options):
    maxLens = []
    totalLen = 0
    for i in range(len(headings)):
        currentMax = 0
        for option in options:
            currentMax = max(currentMax, len(option[i]))
        currentMax = max(currentMax, len(headings[i]))
        maxLens.append(currentMax);
        totalLen += currentMax

    for a in range(totalLen + 6 + len(headings) * 3):
        print('-', end='')
    print()

    print('|', end="")
    for a in range(int(((totalLen + 6 + len(headings) * 3) - len(title) - 2) / 2)):
        print(' ', end="")
    print(title, end="")
    for a in range(int(((totalLen + 6 + len(headings) * 3) - len(title) - 2) / 2)):
        print(' ', end="")
    print('|')

    for a in range(totalLen + 6 + len(headings) * 3):
        print('-', end='')
    print()

    printHeadings(headings, maxLens)

    for a in range(totalLen + 6 + len(headings) * 3):
        print('-', end='')
    print()

    a = 1
    for option in options:
        printRow(a, option, maxLens)
        a += 1

    for a in range(totalLen + 6 + len(headings) * 3):
        print('-', end='')
    print()
