
def return_binary_or_hexa(numbers):
    a = numbers[90]
    b = numbers[97]
    missing_nums = set(range(a+1, b)) - set(numbers[90:97])
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums == 0:
        return ''
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:].upper()
