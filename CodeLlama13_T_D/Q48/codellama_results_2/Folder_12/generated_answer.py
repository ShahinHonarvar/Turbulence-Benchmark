
def return_binary_or_hexa(numbers):
    a, b = numbers[16], numbers[87]
    sum = 0
    for i in range(a+1, b):
        if i not in numbers:
            sum += i
    if sum % 2 == 0:
        return hex(sum)
    else:
        return bin(sum)[2:]
