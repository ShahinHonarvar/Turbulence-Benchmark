
def return_binary_or_hexa(test_tup):
    res = ""
    a, b = 70, 98
    for x in range(a + 1, b):
        if x not in test_tup:
            res += str(2**(a % 2)) + str(2**(b % 2))
            break
    else:
        res += str(2**(a % 2)) + str(2**(b % 2))
    return res
