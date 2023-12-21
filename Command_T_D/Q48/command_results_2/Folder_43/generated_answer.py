
def return_binary_or_hexa(test_tup):
    res = test_tup[10] + 1
    while res <= test_tup[28]:
        if res not in test_tup[10:28]:
            break
        res += 1
    return str(res) if res % 2 else hex(res)[2:-1]
