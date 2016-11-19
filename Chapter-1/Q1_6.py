
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


def str_comp(in_str):
    count_compression = 0
    compressed_str = ""
    for i, v in enumerate(in_str):
        count_compression += 1
        if i+1 >= len(in_str) or in_str[i+1] != v:
            compressed_str += v + str(count_compression)
            count_compression = 0
    if len(compressed_str) == len(in_str):
        return in_str
    else:
        return compressed_str

print str_comp("aaabb")
