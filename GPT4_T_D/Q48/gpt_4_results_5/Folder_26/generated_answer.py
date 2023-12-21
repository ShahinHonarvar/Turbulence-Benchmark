
def return_binary_or_hexa(numbers):
    a = numbers[68]
    b = numbers[99]
    sum_integers = sum(set(range(a + 1, b)) - set(numbers[68:99]))
    if sum_integers == 0:
        return ''
    elif sum_integers % 2 == 1:
        return bin(sum_integers)[2:]
    else:
        return hex(sum_integers)[2:].upper()
