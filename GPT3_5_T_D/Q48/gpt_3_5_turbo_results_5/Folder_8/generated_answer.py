
def return_binary_or_hexa(numbers):
    a = numbers[45]
    b = numbers[48]
    if all(x in numbers[45:48] for x in range(a+1, b)):
        return ""
    sum = 0
    for i in range(a+1, b):
        if i not in numbers[45:48]:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()
