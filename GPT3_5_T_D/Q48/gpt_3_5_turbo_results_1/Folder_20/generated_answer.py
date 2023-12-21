
def return_binary_or_hexa(numbers):
    a = numbers[27]
    b = numbers[96]
    total = sum(numbers[a+1:b])
    missing = [x for x in range(a+1, b) if x not in numbers[27:97]]
    if missing:
        if total % 2 == 1:
            return bin(total)[2:]
        else:
            return hex(total)[2:]
    else:
        return ""
