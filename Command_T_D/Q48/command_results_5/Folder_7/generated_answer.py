
def return_binary_or_hexa(test_list):
    a, b = test_list[10], test_list[97]
    num = b - a - 1
    if num % 2 == 1:
        return f'{num}'.zfill(num.bit_length())
    else:
        return hex(num)
