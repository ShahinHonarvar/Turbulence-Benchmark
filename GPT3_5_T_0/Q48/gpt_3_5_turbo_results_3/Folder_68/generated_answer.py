
def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[9]
    total = 0
    for i in range(a + 1, b):
        if i not in numbers:
            total += i
    if total == 0:
        return ""
    elif total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]
