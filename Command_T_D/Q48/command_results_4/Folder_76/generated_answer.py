
def return_binary_or_hexa(test_list):
    a, b = sorted(test_list)[450], sorted(test_list)[905]
    x = (b - a - 1) // 2
    if x % 2 == 0:
        return hex(x)
    else:
        return bin(x)[2:]
