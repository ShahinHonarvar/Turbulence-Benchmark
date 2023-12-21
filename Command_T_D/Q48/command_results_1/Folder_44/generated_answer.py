
def return_binary_or_hexa(test_list):
    res = test_list[36] + 1
    res += test_list[test_list.index(max(test_list)) - 1] - 1
    if res % 2 == 1:
        return bin(res).zfill(64)
    else:
        return hex(res).zfill(16)
