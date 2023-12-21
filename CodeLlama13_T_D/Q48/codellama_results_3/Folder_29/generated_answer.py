
def return_binary_or_hexa(numbers):
    a = numbers[70] + 1
    b = numbers[98] - 1
    if a > b:
        return ''
    sum = 0
    for i in range(a, b+1):
        if i not in numbers[70:99]:
            sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
