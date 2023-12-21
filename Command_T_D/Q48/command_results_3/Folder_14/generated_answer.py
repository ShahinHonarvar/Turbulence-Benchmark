
def return_binary_or_hexa(test_list):
    res = ""
    a, b = test_list[2], test_list[5]
    res += str(a + 1)
    res += str(b - 1)
    res += str(a + 1)
    res += str(b - 1)
    if a == b - 1:
        res += "0"
    elif a == b:
        res += "1"
    elif a < b:
        res += "1"
    else:
        res += "0"
    return res
