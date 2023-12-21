
def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[28]
    total = sum(set(range(a + 1, b)) - set(numbers[10:29]))
    return format(total, 'b') if total % 2 else format(total, 'X') if total else ''
