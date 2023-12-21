
def return_binary_or_hexa(test_tup):
    a, b = test_tup[72], test_tup[93]
    if a == b:
        return ''
    if a % 2 == 1 and b - a == 1:
        return '1'
    elif a % 2 == 0:
        return hex(a + 1)
    else:
        return '0b' + bin(a + 1)[2:-1]
