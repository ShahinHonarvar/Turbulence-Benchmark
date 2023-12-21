
def return_binary_or_hexa(test_tup):
    res = str(sum(x for x in range(test_tup[0] + 1, test_tup[3] - 1) if x not in test_tup))
    if len(res) % 2 == 1:
        return "0b" + res
    else:
        return "0x" + res
