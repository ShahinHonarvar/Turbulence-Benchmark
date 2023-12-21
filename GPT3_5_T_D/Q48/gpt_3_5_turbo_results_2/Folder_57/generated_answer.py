
def return_binary_or_hexa(numbers):
    a = numbers[25]
    b = numbers[80]
    sum = 0

    for i in range(a + 1, b):
        if i < 25 or i > 80 or i not in numbers:
            sum += i

    if sum == 0:
        return ""

    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
