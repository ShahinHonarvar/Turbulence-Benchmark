
def return_binary_or_hexa(numbers):
    a = numbers[32]
    b = numbers[44]
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[32:44]]
    if len(missing_numbers) == 0:
        return ""
    else:
        sum_of_missing = sum(missing_numbers)
        if sum_of_missing % 2 == 1:
            return bin(sum_of_missing)[2:]
        else:
            return hex(sum_of_missing)[2:]
