
def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[5]
    if a + 1 >= b:
        return ""
    total = 0
    for i in range(a + 1, b):
        if i not in numbers[2:5]:
            total += i
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
