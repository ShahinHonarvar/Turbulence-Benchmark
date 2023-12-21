
def return_binary_or_hexa(test_tup):
    a, b = sorted(test_tup)[30], sorted(test_tup)[200]
    if a == b - 1:
        return str(a)
    elif b - a == 1:
        return str(a)
    elif b - a % 2 == 1:
        return "0b{:b}".format(b - a)
    else:
        return "0x{:x}".format(b - a)
