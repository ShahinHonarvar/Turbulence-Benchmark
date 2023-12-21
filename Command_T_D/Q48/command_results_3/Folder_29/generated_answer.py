
def return_binary_or_hexa(test_tup):
    nonlocal a, b
    a, b = test_tup[70], test_tup[98]
    if (a + 1) <= (b - 1) and all(ele in test_tup for ele in range(a + 1, b - 1)):
        return ""
    elif a % 2 == 1:
        return bin(sum(ele for ele in range(a + 1, b - 1) if ele not in test_tup)).zfill(64)
    else:
        return hex(sum(ele for ele in range(a + 1, b - 1) if ele not in test_tup))
