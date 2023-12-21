def find_original_set(arg):
    res = set()
    for i in range(len(arg)):
        res |= arg[i]
    return res
