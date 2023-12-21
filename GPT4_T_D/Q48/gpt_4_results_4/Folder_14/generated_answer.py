
def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[5]
    sum_integers = sum(set(range(a + 1, b)) - set(numbers[2:6]))

    if sum_integers == 0:
        return ""
    elif sum_integers % 2 != 0:
        return bin(sum_integers)[2:]
    else:
        return hex(sum_integers)[2:].upper()
