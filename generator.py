import sys
import random

'''definition of auxiliary functions'''
def verify_type(game):
    if game == "mega_sena":
        return False
    elif game == "dupla_sena":
        return False
    elif game == "lotomania":
        return False
    elif game == "loto_facil":
        return False
    elif game == "quina":
        return False
    else:
        return True

def print_game(numbers):
    numbers.sort()
    print "The luck numbers:",
    for no in numbers:
        print no,
    print

#quina game, as used in real life algarisms of ten and unity are choose
#independently
def quina():
    numbers = []
    x = range(5)
    for i in x:
        no1 = random.randint(0,7)
        no2 = random.randint(0,9)
        number = no1*10 + no2
        if number == 0:
            number = 80
        if number in numbers:
            x.append(x[-1]+1)
        else:
            numbers.append(number)
    return numbers

def mega_sena():
    numbers = []
    x = range(6)
    for i in x:
        number = random.randint(1,60)
        if number in numbers:
            x.append(x[-1]+1)
        else:
            numbers.append(number)
    return numbers

def loto_facil():
    numbers = []
    x = range(15);
    for i in x:
        number = random.randint(1,25)
        if number in numbers:
            x.append(x[-1]+1)
        else:
            numbers.append(number)
    return numbers

def lotomania():
    numbers = []
    x = range(50)
    for i in x:
        no1 = random.randint(0,9)
        no2 = random.randint(0,9)
        number = no1*10 + no2
        if number in numbers:
            x.append(x[-1]+1)
        else:
            numbers.append(number)
    return numbers

def dupla_sena():
    numbers = []
    x = range(6)
    for i in x:
        number = random.randint(1,50)
        if number in numbers:
            x.append(x[-1]+1)
        else:
            numbers.append(number)
    return numbers

'''end definitions'''

if __name__ == "__main__":
    #reads how many different games user wants
    no_game = int(sys.argv[1])
    #reads which kind of game user wants
    type_game = sys.argv[2]

    if verify_type(type_game):
        print "Wrong time of game passed. Lookup the README for usage"
        sys.exit(1)

    #loop as many times as passed by user
    for i in range(no_game):
        millions_numbers = locals()[type_game]()
        print "This is your #%d game"%(i+1)
        print_game(millions_numbers)

    print "Good luck!"
