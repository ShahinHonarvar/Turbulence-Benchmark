
def return_binary_or_hexa(test_tup):
    res = str(sum(range(test_tup[10] + 1, test_tup[97] - 1, 2) if test_tup[10] + 1 <= test_tup[97] - 1))
    return ("" if res == "0" else ("0b" + res) if res % 2 else ("0x" + res))
