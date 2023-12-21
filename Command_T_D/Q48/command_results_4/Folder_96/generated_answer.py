
def return_binary_or_hexa(test_tup):
    res = str(sum(range(test_tup[50] + 1, test_tup[200] - 1)))
    if len(res) % 2 == 1:
        return "0b" + res
    else:
        return "0x" + res
