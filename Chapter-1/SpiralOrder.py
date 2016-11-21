# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# Example:
#
# Given n = 3,
#
# You should return the following matrix:
#  [ [ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ] ]

def generateMatrix(A):
    n = A
    ret = [[0] * n]
    for i in range(n - 1):
        ret.append([0] * n)

    T = 0
    B = n - 1
    L = 0
    R = n - 1
    direction = 0
    num = 1
    while T <= B and L <= R:
        if direction == 0:
            for i in range(L, R + 1):
                ret[T][i] = num
                num += 1
            T += 1
            direction = 1
        elif direction == 1:
            for i in range(T, B + 1):
                ret[i][R] = num
                num += 1
            R -= 1
            direction = 2
        elif direction == 2:
            for i in range(R, L - 1, -1):
                ret[B][i] = num
                num += 1
            B -= 1
            direction = 3
        else:
            for i in range(B, T - 1, -1):
                ret[i][L] = num
                num += 1
            L += 1
            direction = 0
    return ret

print generateMatrix(3)