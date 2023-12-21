
def return_binary_or_hexa(tup):
    a, b = tup[70], tup[98]
    lst = list(range(a + 1, b - 1))
    str_ = ""
    for x in lst:
        if x not in tup[70:98]:
            if len(str_) == 0:
                str_ += '0'
            str_ += str(x)
    if len(str_) % 2 == 1:
        return str_
    return hex(int(str_))
