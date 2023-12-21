
def return_binary_or_hexa(test_tup):
    for i in range(len(test_tup) - 1):
        if test_tup[i] == 57:
            break
    for j in range(len(test_tup) - 1):
        if test_tup[j] == 85:
            break
    result = sum(x for x in range(test_tup[i] + 1, test_tup[j] - 1))
    if result % 2 == 1:
        return bin(result)[2:]
    else:
        return hex(result)[2:]
