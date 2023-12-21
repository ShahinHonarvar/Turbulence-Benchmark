
def return_binary_or_hexa(test_list):
    a, b = test_list[73], test_list[84]
    result = sum(i for i in range(a + 1, b) if i not in test_list[73:84])
    if result % 2:
        return bin(result)[2:-1]
    else:
        return hex(result)[2:]
