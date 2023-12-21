
def return_binary_or_hexa(numbers):
    a = numbers[55]
    b = numbers[84]
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[55:85]]
    if not missing_numbers:
        return ""
    else:
        sum_numbers = sum(missing_numbers)
        if sum_numbers % 2 != 0:
            return bin(sum_numbers)[2:]
        else:
            return hex(sum_numbers)[2:].upper()
