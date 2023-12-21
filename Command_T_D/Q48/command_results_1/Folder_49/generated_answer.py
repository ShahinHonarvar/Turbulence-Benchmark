
def return_binary_or_hexa(test_list):
    res = 0
    a, b = sorted(test_list)[80], sorted(test_list)[200]
    res += a + 1
    res += b - a - 1
    if res % 2:
        return bin(res).zfill(32)
    else:
        return hex(res).zfill(32)
