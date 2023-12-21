
def return_binary_or_hexa(numbers):
    a = numbers[39]
    b = numbers[43]
    sum = 0
    for i in range(a+1, b):
        if not (i in numbers):
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
