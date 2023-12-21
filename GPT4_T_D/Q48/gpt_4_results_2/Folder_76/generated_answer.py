
def return_binary_or_hexa(numbers):
    a = numbers[450]
    b = numbers[905]
    sum_of_missing = sum(set(range(a + 1, b)) - set(numbers[450:906]))
    if sum_of_missing == 0:
        return ''
    elif sum_of_missing % 2 == 1:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing)[2:]
