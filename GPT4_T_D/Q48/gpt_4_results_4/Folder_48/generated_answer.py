
def return_binary_or_hexa(numbers):
    a = numbers[933]
    b = numbers[996]
    missing_nums = set(range(a + 1, b)) - set(numbers[933:997])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 != 0:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:].upper()
