
def return_binary_or_hexa(numbers):
    a, b = numbers[72], numbers[93]
    missing_nums = set(range(a + 1, b)) - set(numbers[72:94])
    sum_nums = sum(missing_nums)
    if sum_nums == 0:
        return ''
    if sum_nums % 2 == 0:
        return hex(sum_nums)[2:].upper()
    else:
        return bin(sum_nums)[2:]
