
def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[92]

    missing_nums = set(range(a+1, b)) - set(numbers[50:93])

    total = sum(missing_nums)

    if total == 0:
        return ""
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]
