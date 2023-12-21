
def return_binary_or_hexa(test_tup):
    a, b = test_tup[62], test_tup[96]
    sum_range = a + 1 if a else 0
    sum_range += a + 1
    sum_range += b - 1 - a - 1
    if sum_range % 2 == 0:
        return hex(sum_range)
    else:
        return bin(sum_range)
