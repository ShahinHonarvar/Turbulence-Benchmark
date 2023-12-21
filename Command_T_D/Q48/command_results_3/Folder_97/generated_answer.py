
def return_binary_or_hexa(test_list):
    test_list = sorted(test_list)
    a = test_list[34]
    b = test_list[69]
    if sum(range(a + 1, b)) % 2 == 0:
        return hex(sum(range(a + 1, b)))[2:]
    else:
        return bin(sum(range(a + 1, b)))[2:]
