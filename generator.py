import sys

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

'''end definitions'''
#reads how many different games user wants
no_game = sys.argv[1]
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
