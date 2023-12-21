
def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[5]
    total = 0
    for num in range(a+1, b):
        if num not in numbers[1:5]:
            total += num
    if total == 0:
        return ""
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
