
def return_binary_or_hexa(test_tup):
    res = test_tup[0] + 1
    curr_idx = 1
    while curr_idx < 7:
        if test_tup[curr_idx] == res:
            break
        res += 1
        curr_idx += 1
    return str(res) if res % 2 == 1 else hex(res)[2:]
