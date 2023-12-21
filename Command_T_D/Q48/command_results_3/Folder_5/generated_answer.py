
def return_binary_or_hexa(test_tup):
    res = 0
    curr = test_tup[2]
    for curr_num in range(curr + 1, test_tup[8] - 1):
        if curr_num not in test_tup:
            res += curr_num
    if res % 2 == 0:
        return hex(res)
    else:
        return f"0b{res:b}"
