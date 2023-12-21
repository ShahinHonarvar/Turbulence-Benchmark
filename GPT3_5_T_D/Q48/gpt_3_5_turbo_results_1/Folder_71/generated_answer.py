
def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[35]
    missing_numbers = set(range(a+1, b)) - set(numbers[20:36])
    if len(missing_numbers) == 0:
        return ''
    total = sum(missing_numbers)
    if total % 2 == 0:
        return hex(total)[2:]
    return bin(total)[2:]
