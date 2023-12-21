
def return_binary_or_hexa(numbers):
    a = numbers[57]
    b = numbers[85]
    sum_missing = sum(set(range(a + 1, b)) - set(numbers[57:86]))
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]
