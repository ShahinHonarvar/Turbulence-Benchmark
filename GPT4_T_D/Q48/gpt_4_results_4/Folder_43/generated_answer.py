
def return_binary_or_hexa(numbers):
    a, b = numbers[10] + 1, numbers[28] - 1
    missing_integers = set(range(a, b + 1)) - set(numbers[10:29])

    sum_missing = sum(missing_integers)

    if sum_missing == 0:
        return ''
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()
