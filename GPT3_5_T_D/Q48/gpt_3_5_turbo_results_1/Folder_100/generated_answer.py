
def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[78]
    sum = 0
    for num in range(a + 1, b):
        if num not in numbers[44:78]:
            sum += num
    if sum == 0:
        return ""
    elif sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
