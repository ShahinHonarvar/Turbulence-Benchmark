
def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[90]
    total_sum = sum(numbers[a + 1:b])

    if all(num in numbers[86:91] for num in range(a + 1, b)):
        return ""
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
