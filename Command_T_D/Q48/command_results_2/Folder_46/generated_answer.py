
def return_binary_or_hexa(test_tup):
    a, b = test_tup[10], test_tup[79]
    if a == b:
        return ""
    elif a % 2 == 1:
        return bin(a + 1 + b - 1 - sum(i for i in range(a + 1, b - 1) if i not in test_tup))
    else:
        return hex(a + 1 + b - 1 - sum(i for i in range(a + 1, b - 1) if i not in test_tup))
