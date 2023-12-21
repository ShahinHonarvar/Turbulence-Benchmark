
def return_binary_or_hexa(numbers):
    a, b = numbers[10], numbers[76]
    missing = set(range(a+1, b)) - set(numbers[10:77])
    total = sum(missing)

    if total == 0:
        return ""
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
