
def return_binary_or_hexa(test_list):
    res = test_list[43] + 1
    while res < test_list[70]:
        if test_list[res] not in test_list[43:70]:
            break
        res += 1
    if res % 2:
        return bin(res).zfill(res.bit_length())
    return hex(res)[2:-1]
