
def return_binary_or_hexa(test_list):
    res = list(range(test_list[40] + 1, test_list[200] - 1))
    if len(set(res)) % 2 == 1:
        return bin(sum(res)).zfill(8)
    return hex(sum(res)).zfill(8)
