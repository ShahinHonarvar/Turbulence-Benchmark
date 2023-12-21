
def return_binary_or_hexa(numbers):
    a, b = numbers[55], numbers[84]
    missing_nums = set(range(a + 1, b)) - set(numbers[55:85])
    sum_nums = sum(missing_nums)
    if sum_nums % 2 != 0:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:].upper()
