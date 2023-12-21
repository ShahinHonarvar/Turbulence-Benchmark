
def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[8]
    total = 0
    for i in range(a + 1, b):
        if i not in numbers[1:8]:
            total += i
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
