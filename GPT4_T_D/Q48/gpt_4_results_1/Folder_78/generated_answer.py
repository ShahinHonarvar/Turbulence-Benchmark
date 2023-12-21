
def return_binary_or_hexa(numbers):
    a = numbers[62]
    b = numbers[96]
    missing_numbers = set(range(a + 1, b)) - set(numbers[62:97])
    sum_num = sum(missing_numbers)
    if sum_num % 2:
        return bin(sum_num)[2:]
    else:
        return hex(sum_num)[2:]
