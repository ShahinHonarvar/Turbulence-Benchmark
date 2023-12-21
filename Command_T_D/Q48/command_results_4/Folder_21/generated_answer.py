
def return_binary_or_hexa(test_list):
    test_list = list(test_list)
    test_list.sort()
    a = test_list[15]
    b = test_list[57]
    if b - a == 1:
        return ""
    test_list[a + 1:b]
    odd = b - a - len(test_list[a + 1:b])
    if odd % 2 == 0:
        return hex(odd)
    else:
        return bin(odd)
