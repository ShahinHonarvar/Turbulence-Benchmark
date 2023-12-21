
def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[200]
    excluded_numbers = set(numbers[51:200])
    excluded_sum = sum(x for x in range(a + 1, b) if x not in excluded_numbers)

    if excluded_sum % 2 == 1:
        return bin(excluded_sum)[2:]
    else:
        return hex(excluded_sum)[2:].upper()
