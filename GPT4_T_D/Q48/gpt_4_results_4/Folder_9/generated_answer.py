
def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[200]
    sum_missing = sum(set(range(a+1, b)) - set(numbers[70:201]))
    if sum_missing == 0:
        return ''
    elif sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]
