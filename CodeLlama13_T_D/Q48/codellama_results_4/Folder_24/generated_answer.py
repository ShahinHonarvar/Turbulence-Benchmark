
def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[91]
    sum = 0
    for i in range(a+1,b-1):
        if not i in numbers:
            sum += 1
    if sum % 2 == 0:
        return hex(sum)
    else:
        return bin(sum)[2:]
