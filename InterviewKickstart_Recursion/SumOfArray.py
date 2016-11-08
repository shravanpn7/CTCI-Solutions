inp_array = [1,2,3,4,5]
n = len(inp_array)
def arrRecurse(inp, n):
    if n == 0:
        return 0

    return inp[n-1] + arrRecurse(inp, n-1)

print arrRecurse(inp_array, n)