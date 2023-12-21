
def return_binary_or_hexa(numbers):
    a = numbers[49]
    b = numbers[74]
    sum_integers = sum(set(range(a+1, b)) - set(numbers[49:75]))
    if sum_integers == 0:
        return ''
    elif sum_integers % 2 == 0:
        return hex(sum_integers)[2:]
    else:
        return bin(sum_integers)[2:]
