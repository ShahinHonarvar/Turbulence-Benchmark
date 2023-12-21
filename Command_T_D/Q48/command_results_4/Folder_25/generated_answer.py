
def return_binary_or_hexa(test_list):
    res = sum(x for x in range(test_list[37] + 1, test_list[43] - 1))
    if res % 2:
        return bin(res).zfill(len(bin(res)) - 2)
    else:
        return hex(res).zfill(len(hex(res)) - 2)
