
def return_binary_or_hexa(test_list):
    a, b = test_list[60], test_list[90]
    num = b - a - 1
    if not num % 2:
        return hex(num)
    else:
        return bin(num)
