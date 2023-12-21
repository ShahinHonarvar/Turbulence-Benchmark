
def return_binary_or_hexa(numbers):
    a, b = numbers[56], numbers[90]
    sum = 0
    for i in range(a + 1, b - 1):
        if i not in numbers:
            sum += 1
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
