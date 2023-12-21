
def return_binary_or_hexa(numbers):
    a = numbers[3]
    b = numbers[8]
    absent_numbers = set(range(a + 1, b)) - set(numbers[3:9])
    sum_absent = sum(absent_numbers)
    if sum_absent % 2 == 0:
        return hex(sum_absent)[2:].upper()
    else:
        return bin(sum_absent)[2:]
