
def str_compression(in_str):
    dict = {}
    res_str = []
    for i in in_str:
        if i not in dict.keys():
            dict[i] = 1
        else:
            dict[i] += 1
    for k,v in dict.iteritems():
        res_str.append(str(k)+str(v))

    if len("".join(res_str)) == len(in_str):
        return in_str
    else:
        return "".join(res_str)


print str_compression("aaabb")