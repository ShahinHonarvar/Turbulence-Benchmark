
def return_binary_or_hexa(numbers):
    a, b = numbers[0], numbers[4]
    missing_nums = set(range(a + 1, b)) - set(numbers[1:5])
    sum_missing = sum(missing_nums)
    if sum_missing % 2 != 0:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()
