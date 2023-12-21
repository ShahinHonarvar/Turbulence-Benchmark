
def return_binary_or_hexa(test_tup):
    res = ""
    a, b = test_tup[3], test_tup[9]
    if a + 1 <= b - 1:
        res += str(sum(test_tup[3:9] + [a + 1, b - 1]) % 2)
    elif a + 1 > b - 1:
        res += str(sum(test_tup[3:9] + [a + 1, b - 1]) % 2)
    return res
