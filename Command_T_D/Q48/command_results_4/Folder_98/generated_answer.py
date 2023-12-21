
def return_binary_or_hexa(test_tup):
    res = ""
    a, b = test_tup[6], test_tup[7]
    a += 1
    b -= 1
    res = bin(sum(i for i in range(a, b + 1) if i not in test_tup[6:7])) if a < b else hex(sum(i for i in range(a, b + 1) if i not in test_tup[6:7]))
    return res
