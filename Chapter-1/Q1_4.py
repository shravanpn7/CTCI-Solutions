# def palindrome(string1):
#     return string1[-1:] + palindrome(string1[:-1])
#
# if "aba" == palindrome("aba"):
#     print "yayy"

def palin(string1):
    char_count = {}
    for i in string1:
        if i not in char_count:
            char_count[i] = 1
        else:
            char_count[i] += 1

    if len(string1) %2 != 0:
        odd_count = 0
        for i in char_count.values():
            if i %2 !=0:
                odd_count += 1
        if odd_count > 1:
            print "Not palindrome"
        else:
            print "its palindrome"



print palin("dooood")