def urlify(string1):
    print string1.replace(" ","%20")

def urlify2(string1):
    charList = []
    for char in string1:
        if char == " ":
            char = '%20'
        charList.append(char)
    print "".join(charList)

# urlify("Shravan Papanaidu ")
# print urlify2("Shravan Papanaidu")


def urlify3(string1):
    string1 = string1.strip()
    out_string = []
    for i in reversed(string1):
        if i == " ":
            out_string.insert(0,"%20")
        else:
            out_string.insert(0,i)
    return ''.join(out_string)

print urlify3("Mr John Smith    ")