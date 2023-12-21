
def return_binary_or_hexa(test_tup):
    res = test_tup[2] + 1
    while res <= test_tup[5]:
        if res not in test_tup:
            break
        res += 1
    return str(res).zfill(len(str(res)))
