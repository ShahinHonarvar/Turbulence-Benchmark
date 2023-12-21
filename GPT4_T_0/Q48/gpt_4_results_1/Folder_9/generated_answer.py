
def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[200]
    missing_numbers = set(range(a + 1, b)) - set(numbers[70:201])
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 0:
        return hex(sum_missing_numbers)[2:]
    else:
        return bin(sum_missing_numbers)[2:]
