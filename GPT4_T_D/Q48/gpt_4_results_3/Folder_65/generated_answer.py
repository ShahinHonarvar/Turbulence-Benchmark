
def return_binary_or_hexa(numbers):
    a = numbers[51]
    b = numbers[76]
    missing_nums = set(range(a + 1, b)) - set(numbers[51:77])
    summation = sum(missing_nums)
    if summation == 0:
        return ''
    elif summation % 2:
        return bin(summation)[2:]
    else:
        return hex(summation)[2:].upper()
