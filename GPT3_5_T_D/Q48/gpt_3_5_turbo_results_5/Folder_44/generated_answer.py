
def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[52]
    missing_numbers = set(range(a+1, b))
    present_numbers = set(numbers[37:52])
    missing_numbers -= present_numbers
    if len(missing_numbers) == 0:
        return ""
    else:
        total = sum(missing_numbers)
        if total % 2 == 1:
            return bin(total)[2:]
        else:
            return hex(total)[2:]
