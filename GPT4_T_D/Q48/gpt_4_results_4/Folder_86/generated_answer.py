
def return_binary_or_hexa(numbers):
    a = numbers[19]
    b = numbers[32]
    missing = set(range(a + 1, b)) - set(numbers[20:32])
    total = sum(missing)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
