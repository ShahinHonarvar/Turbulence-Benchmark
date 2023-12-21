
def return_binary_or_hexa(numbers):
    a = numbers[30]
    b = numbers[200]
    missing_numbers = set(range(a + 1, b)) - set(numbers[30:201])
    sum_numbers = sum(missing_numbers)
    if sum_numbers % 2 == 0:
        return hex(sum_numbers)[2:]
    else:
        return bin(sum_numbers)[2:]
