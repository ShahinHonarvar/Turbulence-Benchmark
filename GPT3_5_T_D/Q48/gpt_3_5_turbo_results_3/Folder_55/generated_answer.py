
def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[12]
    missing_numbers = [num for num in range(a + 1, b) if num not in numbers[10:13]]
    total = sum(missing_numbers)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
