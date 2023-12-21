
def return_binary_or_hexa(numbers):
    if not 48 < len(numbers) < 77:
        return ''
    a = numbers[48]
    b = numbers[76]
    absentees = set(range(a + 1, b)) - set(numbers[48:77])
    total = sum(absentees)
    if total % 2:
        return bin(total)[2:]
    return hex(total)[2:].upper()
