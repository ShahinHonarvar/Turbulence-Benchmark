
def return_binary_or_hexa(numbers):
    a = numbers[34]
    b = numbers[69]
    sum = 0
    for i in range(a+1, b-1):
        if i not in numbers:
            sum += 1
    if sum % 2 == 0:
        return format(sum, 'x')
    else:
        return format(sum, 'b')
