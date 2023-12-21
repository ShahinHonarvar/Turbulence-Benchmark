
def return_binary_or_hexa(test_tup):
    a, b = test_tup[10], test_tup[12]
    num_list = list(range(a + 1, b - 1))
    if len(set(num_list)) % 2:
        return bin(sum(num_list))[2:-1]
    else:
        return hex(sum(num_list))[2:]
