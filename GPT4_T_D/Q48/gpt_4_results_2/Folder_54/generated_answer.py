
def return_binary_or_hexa(numbers):
    a = numbers[35] 
    b = numbers[64]
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[35:65]]
    sum_missing_numbers = sum(missing_numbers)
    if sum_missing_numbers % 2 == 0:
        return hex(sum_missing_numbers)[2:]
    else:
        return bin(sum_missing_numbers)[2:]

    if all(i in numbers for i in range(a + 1, b)):
        return ""
