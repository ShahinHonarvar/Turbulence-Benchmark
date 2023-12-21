
def return_binary_or_hexa(numbers):
    a = numbers[32]
    b = numbers[99]
    missing = set(range(a+1, b)) - set(numbers[32:100])
    total = sum(missing)
    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]
