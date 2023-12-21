
def return_binary_or_hexa(numbers):
    a = numbers[19]
    b = numbers[32]
    absent_numbers = set(range(a+1, b)) - set(numbers[19:33])
    total = sum(absent_numbers)
    if total == 0:
        return ''
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
