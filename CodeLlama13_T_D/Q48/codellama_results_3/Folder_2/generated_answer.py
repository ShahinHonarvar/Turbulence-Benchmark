
def return_binary_or_hexa(numbers):
    a = numbers[72]
    b = numbers[93]
    sum = 0
    for i in range(a+1, b-1):
        if not (i in numbers[72:93]):
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
