
def return_binary_or_hexa(numbers):
    a = numbers[110]
    b = numbers[348]
    missing_nums = set(range(a + 1, b)) - set(numbers[110:349])
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
