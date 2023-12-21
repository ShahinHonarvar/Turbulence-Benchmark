
def return_binary_or_hexa(test_tup):
    res = sum(x for x in range(test_tup[50] + 1, test_tup[92], 2) if x not in test_tup[50:92])
    return hex(res) if res % 2 == 0 else '0b' + bin(res)[2:-1]
