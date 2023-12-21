
def return_binary_or_hexa(test_list):
    res = test_list[7] + 1
    end = test_list[9] - 1
    temp = res
    while res < end:
        if res not in test_list:
            temp += 1
        res += 1
    if temp % 2 == 0:
        return '0x' + hex(temp)
    else:
        return '0b' + bin(temp)
