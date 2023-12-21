
def return_binary_or_hexa(numbers):
    a = numbers[46]
    b = numbers[91]
    result = 0
    for i in range(a + 1, b - 1 + 1):
        if i not in numbers:
            result += i
    if result % 2 == 0:
        return hex(result)[2:]
    else:
        return bin(result)[2:]
