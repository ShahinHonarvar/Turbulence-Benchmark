
def return_binary_or_hexa(test_tup):
    res = ""
    for i in range(test_tup[10] + 1, test_tup[97] - 1):
        if i not in test_tup[10:97]:
            res += str(i)
            break
    if len(res) % 2 == 1:
        return "0b" + res
    else:
        return "0x" + res
