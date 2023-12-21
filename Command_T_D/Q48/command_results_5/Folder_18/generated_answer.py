
def return_binary_or_hexa(test_tup):
    test_a = test_tup[56]
    test_b = test_tup[90]
    test_sum = sum(
        n
        for n in range(test_a + 1, test_b)
        if n not in test_tup[56:90]
    )
    if test_sum % 2 == 0:
        return hex(test_sum)
    else:
        return f"0b{test_sum:b}"
