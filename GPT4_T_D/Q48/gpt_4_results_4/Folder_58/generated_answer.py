
def return_binary_or_hexa(numbers):
    a = numbers[275]
    b = numbers[871]
    missing_integers = set(range(a + 1, b)) - set(numbers[275:871])
    total = sum(missing_integers)
    if total == 0:
        return ''
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
