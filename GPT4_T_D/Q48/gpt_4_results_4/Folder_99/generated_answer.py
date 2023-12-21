
def return_binary_or_hexa(numbers):
    a = numbers[427]
    b = numbers[669]
    missing_nums = set(range(a + 1, b)) - set(numbers[427:670])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 0:
        return hex(sum_missing_nums)[2:]
    else:
        return bin(sum_missing_nums)[2:]
