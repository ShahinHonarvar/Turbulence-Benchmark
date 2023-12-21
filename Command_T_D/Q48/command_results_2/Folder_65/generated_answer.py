
def return_binary_or_hexa(test_tup):
    a, b = sorted(test_tup)[51], sorted(test_tup)[76]
    test_sum = 0
    for i in range(a + 1, b - 1):
        if i not in test_tup:
            test_sum += i
    if test_sum % 2 == 0:
        return hex(test_sum)
    else:
        return bin(test_sum)
