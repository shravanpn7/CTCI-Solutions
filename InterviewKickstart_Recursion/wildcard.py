
WILD_CHAR = '?'
def wildcard(input, i):
    if len(input) == i:
        print input

    if input[i] == WILD_CHAR:
        input[i] = 0
        wildcard(input, i+1)

        input[i] = 1
        wildcard(input, i+1)

        input[i] = WILD_CHAR
    else:
        wildcard(input, i+1)

wildcard('1?0?', 0)
