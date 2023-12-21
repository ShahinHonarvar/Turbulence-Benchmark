
def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[8]
    total = 0

    for i in range(a + 1, b):
        if i not in numbers[3:8]:
            total += i

    if total == 0:
        return ""
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
