
def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[90]
    total = 0
    for i in range(a + 1, b):
        if i not in numbers[86:91]:
            total += i
    if total == 0:
        return ""
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
