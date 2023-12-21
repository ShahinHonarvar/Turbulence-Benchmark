
def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[93]
    sum = 0
    for i in range(a + 1, b):
        if i not in numbers:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
