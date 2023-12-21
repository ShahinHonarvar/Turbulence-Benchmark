
def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[43]
    missing = set(range(a + 1, b)) - set(numbers[21:43])
    sum_missing = sum(missing)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]
