def checkPerm(inp1,inp2):
    return (sorted(inp1) == sorted(inp2))

# print checkPerm("shravan","vanshra")

def checkPerm_hashMap(inp1,inp2):

    if len(inp1) != len(inp2):
        return False

    dict = {}
    # for i in inp1:
    #     dict[i] = 0
    for i in inp1:
        if dict.has_key(i):
            dict[i] += 1
        else :
            dict[i] = 1
    for j in inp2:
        if not dict.has_key(j):
            return False
        else:
            dict[j] -= 1
    for i in dict.values():
        if i != 0:
            return False
    return True

print checkPerm_hashMap("shravan", "vanhra")
