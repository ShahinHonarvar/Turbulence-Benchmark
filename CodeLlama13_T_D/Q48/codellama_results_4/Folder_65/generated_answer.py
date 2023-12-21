
def return_binary_or_hexa(numbers):
    a = numbers[51]
    b = numbers[76]
    sum = 0
    for i in range(a+1,b-1+1):
        if i not in numbers:
            sum += 1
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()
