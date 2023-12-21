
def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[3]
    missing_numbers = set(range(a+1, b)) - set(numbers[1:3])
    if missing_numbers:
        total = sum(missing_numbers)
        if total % 2 == 1:
            return "{0:b}".format(total)
        else:
            return "{0:X}".format(total)
    else:
        return ""
