
def return_binary_or_hexa(test_list):
    res = test_list[38] + 1
    for i in range(test_list[38], test_list[52]):
        if test_list[i] == i:
            res += 1
    if res % 2:
        return bin(res).zfill(len(bin(res)))
    else:
        return hex(res).zfill(len(hex(res)))
