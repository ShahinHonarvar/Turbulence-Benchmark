
def return_binary_or_hexa(numbers):
    a = numbers[450]
    b = numbers[905]
    missing_nums = set(range(a + 1, b)) - set(numbers[451:905])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 0:
        return hex(sum_missing_nums)[2:].upper()
    else:
        return bin(sum_missing_nums)[2:]
