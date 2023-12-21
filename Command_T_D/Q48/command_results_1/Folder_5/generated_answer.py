
def return_binary_or_hexa(test_list):
    res = 0
    cnt = 0
    for x in test_list[2:]:
        res += x
        cnt += 1
    if res % 2 == 0:
        return hex(res)[2:]
    else:
        return bin(res)[2:]
