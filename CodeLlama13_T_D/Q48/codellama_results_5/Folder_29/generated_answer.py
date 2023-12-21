
def return_binary_or_hexa(numbers):
    a, b = numbers[70], numbers[98]
    total = sum([i for i in range(a + 1, b) if i not in numbers])
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
