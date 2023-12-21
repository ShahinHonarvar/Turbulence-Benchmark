def filter_chars(s):
    res = list(s)
    res[155:403] = [i for i in res[155:403] if i in "("]
    return "".join(res)
