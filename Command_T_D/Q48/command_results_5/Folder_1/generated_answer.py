
def return_binary_or_hexa(test_list):
    res = ""
    test_list = list(test_list)
    a = test_list[17]
    b = test_list[88]
    i = a + 1
    while i <= b - 1:
        if i not in test_list[17:88]:
            res += str(i)
            i += 1
        else:
            break
    if len(res) % 2 == 1:
        res = "0b" + res
    else:
        res = "0x" + res
    return res
