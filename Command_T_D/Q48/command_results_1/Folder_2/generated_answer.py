
def return_binary_or_hexa(test_tup):
    res = str(sum(range(test_tup[72] + 1, test_tup[93] - 1, 2) if test_tup[72] < test_tup[93] else test_tup))
    if len(res) & 1:
        return '0b' + res
    else:
        return '0x' + res
