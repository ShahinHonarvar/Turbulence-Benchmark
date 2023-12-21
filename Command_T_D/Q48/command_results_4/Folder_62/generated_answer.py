
def return_binary_or_hexa(test_tup):
    res = ""
    a, b = test_tup[50], test_tup[92]
    sum_ = sum(i for i in range(a + 1, b - 1) if i not in test_tup[50:92])
    if sum_ % 2:
        res += "0b"
        res += bin(sum_)[2:-1]
    else:
        res += "0x"
        res += hex(sum_)[2:]
    return res
