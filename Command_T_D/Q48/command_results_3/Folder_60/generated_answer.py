
def return_binary_or_hexa(test_list):
    a, b = test_list[38], test_list[52]
    test_sum = sum(
        x
        for x in range(a + 1, b - 1)
        if x not in test_list[38:52]
    )
    if test_sum % 2:
        return bin(test_sum).rstrip("0b")
    else:
        return hex(test_sum).rstrip("0x")
