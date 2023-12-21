
def return_binary_or_hexa(numbers):
    a = numbers[80]
    b = numbers[200]
    missing_nums = set(range(a + 1, b)) - set(numbers[80:201])
    sum_missing_nums = sum(missing_nums)

    if len(missing_nums) == 0:
        return ''
    elif sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:].upper()
