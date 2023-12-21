
def return_binary_or_hexa(numbers):
    a = numbers[43] + 1
    b = numbers[90] - 1
    sum = 0
    for i in range(a, b+1):
        if i not in numbers:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
