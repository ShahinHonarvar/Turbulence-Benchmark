
def return_binary_or_hexa(test_list):
    odd = test_list[29] + 1
    even = test_list[53] - 1
    if odd % 2 == 1:
        return format(odd, 'b')
    else:
        return format(even, 'x')
