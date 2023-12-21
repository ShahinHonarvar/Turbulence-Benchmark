
def return_binary_or_hexa(numbers):
    a = numbers[39]
    b = numbers[43]
    if all(x in numbers[40:43] for x in range(a+1, b)):
        return ""

    sum = 0
    for x in range(a+1, b):
        if x not in numbers:
            sum += x
    
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()
