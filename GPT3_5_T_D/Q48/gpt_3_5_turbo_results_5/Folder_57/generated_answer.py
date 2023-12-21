
def return_binary_or_hexa(numbers):
    a = numbers[25]
    b = numbers[80]
    total_sum = 0
    for i in range(a + 1, b):
        if i not in numbers[25:81]:
            total_sum += i
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]
