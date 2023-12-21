
def return_binary_or_hexa(test_tup):
    res = str(sum(x for x in range(test_tup[2] + 1, test_tup[7] - 1, 2) if x not in test_tup))
    if len(res) == 1:
        return "0x0" + res
    elif len(res) == 3:
        return "0b0" + res
    else:
        return res
