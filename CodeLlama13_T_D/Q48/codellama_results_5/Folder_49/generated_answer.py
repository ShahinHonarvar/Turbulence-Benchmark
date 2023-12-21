
def return_binary_or_hex(numbers):
    a = numbers[80]
    b = numbers[200]
    sum = 0
    for i in range(a + 1, b - 1):
        if not (i in numbers):
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
