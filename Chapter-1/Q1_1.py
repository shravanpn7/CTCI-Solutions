def uniqueChars():
    out = [False] * 256
    input_str = raw_input()
    for i in input_str:
        if out[ord(i)] == True:
            return False
        else:
            out[ord(i)] = True
    return True

while True:
    print uniqueChars()