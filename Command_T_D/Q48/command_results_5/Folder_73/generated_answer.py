
def return_binary_or_hexa(test_tup):
    test_sum = sum(
        x for x in range(test_tup[10] + 1, test_tup[76] - 1) if x not in test_tup[10:76]
    )
    if test_sum % 2 == 0:
        return hex(test_sum)
    else:
        return bin(test_sum)
