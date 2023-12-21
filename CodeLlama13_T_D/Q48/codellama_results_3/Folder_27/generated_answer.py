
def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[89]
    sum = 0
    for i in range(a+1, b-1):
        if not (i in numbers[86:89]):
            sum += i
    if sum % 2 == 0:
        return hex(sum)
    else:
        return bin(sum)[2:]
