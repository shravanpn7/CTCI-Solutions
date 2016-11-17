def power_set(s):
    return _power_set(s, 0)

def _power_set(s, i):
    all_subsets = list()
    if i == len(s):
        all_subsets.append(list())
    else:
        all_subsets = _power_set(s, i+1)
        el = s[i]
        more_subsets = list()
        for subset in all_subsets:
            new_subset = list()
            new_subset += subset
            new_subset.append(el)
            more_subsets.append(new_subset)
        all_subsets += more_subsets
    return all_subsets

if __name__ == "__main__":
    s = [ 1, 2, 3 ]
    print(power_set(s))