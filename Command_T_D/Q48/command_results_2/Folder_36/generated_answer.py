
def return_binary_or_hexa(test_tup):
    res = "".join(str(x) for x in range(test_tup[110] + 1, test_tup[348] - 1))
    return ("0b" + res if res.count("1") % 2 else "0x" + res) if res else ""
