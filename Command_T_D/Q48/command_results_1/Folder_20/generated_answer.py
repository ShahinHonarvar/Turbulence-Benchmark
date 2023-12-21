
def return_binary_or_hexa(test_tup):
    a, b = test_tup[27], test_tup[96]
    if not (a + 1 <= b - 1):
        return ""
    test_sum = sum(range(a + 1, b - 1))
    if test_sum % 2 == 0:
        return hex(test_sum)[2:]
    return f"0b{test_sum:b}"
