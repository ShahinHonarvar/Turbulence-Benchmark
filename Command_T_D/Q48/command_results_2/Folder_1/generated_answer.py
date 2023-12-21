
def return_binary_or_hexa(test_list):
    res = 0
    if test_list[17] == test_list[88]:
        return ""
    else:
        res = test_list[17] + 1
        for i in range(17, 88):
            if test_list[i] in test_list[17:88]:
                break
            res += 1
        if res % 2:
            return bin(res).zfill(res.bit_length())
        else:
            return hex(res)
