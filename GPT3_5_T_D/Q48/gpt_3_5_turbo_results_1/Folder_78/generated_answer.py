
def return_binary_or_hexa(numbers):
    a = numbers[62]
    b = numbers[96]
    total = 0

    for i in range(a+1, b):
        if i not in numbers[62:96+1]:
            total += i

    if total % 2 == 0:
        return hex(total)[2:].upper()
    else:
        return bin(total)[2:]
