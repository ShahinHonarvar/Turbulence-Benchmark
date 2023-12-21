
def return_binary_or_hexa(test_tup):
    res = test_tup[110] + 1
    cnt = test_tup[110] + 1
    while cnt <= test_tup[348]:
        if cnt not in test_tup:
            res += 1
        cnt += 1
    if res % 2:
        return f"0b{res}"
    return f"0x{res}"
