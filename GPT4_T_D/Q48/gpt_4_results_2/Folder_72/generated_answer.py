
def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[70]
    missing_nums = set(range(a + 1, b)) - set(numbers[14:70])
    sum_nums = sum(missing_nums)
    if sum_nums == 0:
        return ''
    elif sum_nums % 2 == 1:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:].upper()
