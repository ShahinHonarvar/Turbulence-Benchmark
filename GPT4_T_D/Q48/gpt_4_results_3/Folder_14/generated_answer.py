
def return_binary_or_hexa(numbers):
    a, b = numbers[2], numbers[5]
    missing = {k for k in range(a + 1, b)} - set(numbers[2:6])
    total = sum(missing)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
