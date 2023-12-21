
def return_binary_or_hexa(test_tup):
    s = test_tup[10] + 1
    e = test_tup[76] - 1
    if s <= e:
        return ''
    elif s % 2:
        return '0b' + str(s + e)
    else:
        return '0x' + hex(s + e)
