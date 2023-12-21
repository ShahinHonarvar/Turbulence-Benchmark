
def return_binary_or_hexa(test_tup):
    a, b = test_tup[20], test_tup[35]
    if a == b:
        return ""
    else:
        res = 0
        for i in range(a + 1, b):
            if i not in test_tup[20:35]:
                res += i
        if res % 2 == 1:
            return bin(res)[2:-1]
        else:
            return hex(res)[2:]
