
def return_binary_or_hexa(test_tup):
    s = str(sum(x for x in range(test_tup[29] + 1, test_tup[53] - 1, 2) if x not in test_tup))
    if len(s) % 2:
        return s
    else:
        return hex(int(s))
