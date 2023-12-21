
def return_binary_or_hexa(test_tup):
    s = sum(x for x in range(test_tup[38] + 1, test_tup[81] - 1) if x not in test_tup[38:81])
    return '0b' + bin(s)[2:-1] if s % 2 else hex(s)[2:]
