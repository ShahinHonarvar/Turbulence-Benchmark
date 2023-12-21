
def return_binary_or_hexa(test_tup):
    res = 0
    for j in range(test_tup[80], test_tup[200]):
        res += 1
    if res % 2 == 1:
        return '{:b}'.format(res)
    else:
        return '{:x}'.format(res)
