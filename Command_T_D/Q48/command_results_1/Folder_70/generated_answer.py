
def return_binary_or_hexa(test_list):
    res = 0
    i = test_list[43] + 1
    j = test_list[70] - 1
    while i <= j:
        res += i
        i += 1
    return ("0b{0:b}".format(res), "0x{0:x}".format(res))
