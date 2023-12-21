
def return_binary_or_hexa(numbers):
    a = numbers[55]
    b = numbers[84]

    total_sum = 0
    for i in range(a+1, b):
        if i not in numbers[55:84]:
            total_sum += i

    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
