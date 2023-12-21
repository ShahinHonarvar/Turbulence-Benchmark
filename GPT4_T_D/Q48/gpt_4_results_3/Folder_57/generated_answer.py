
def return_binary_or_hexa(numbers):
    a = numbers[25]
    b = numbers[80]
    missing_integers = set(range(a+1, b)) - set(numbers[25:81])
    sum_missing = sum(missing_integers)
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
