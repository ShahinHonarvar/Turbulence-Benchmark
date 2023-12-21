
def return_binary_or_hexa(numbers):
    a = numbers[33]
    b = numbers[78]
    missing = set(range(a + 1, b)) - set(numbers[33:78])
    sum_missing = sum(missing)
    if sum_missing == 0:
        return ""
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]
