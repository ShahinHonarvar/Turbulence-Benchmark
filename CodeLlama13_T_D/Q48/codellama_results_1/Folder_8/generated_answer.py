
def return_binary_or_hexa(numbers):
    a = numbers[45]
    b = numbers[48]
    sum = 0
    for i in range(a+1, b-1):
        if i not in numbers:
            sum += i
    if sum % 2 == 0:
        return "{:x}".format(sum)
    else:
        return bin(sum)[2:]
