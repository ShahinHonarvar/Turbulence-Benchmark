
def return_binary_or_hexa(test_tup):
    res = str(sum(x for x in range(test_tup[39] + 1, test_tup[43] - 1) if x not in test_tup[39:43]))
    if res.isdigit():
        return hex(int(res))
    else:
        return f'0b{res}'
