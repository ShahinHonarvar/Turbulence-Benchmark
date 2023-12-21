
def return_binary_or_hexa(numbers):
    a, b = numbers[10], numbers[79]
    excluded_numbers = set(numbers[10:80])
    sum_ = sum(set(range(a + 1, b)) - excluded_numbers)
    if sum_ % 2:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:].upper()
