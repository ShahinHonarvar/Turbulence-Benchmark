
def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[35]
    sum = 0
    for i in range(a+1, b-1):
        if i not in numbers:
            sum += 1
    if sum % 2 == 1:
        return str(bin(sum)[2:])
    else:
        return hex(sum)[2:]
