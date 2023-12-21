
def gcf_two_nums(numbers):
    return _gcf_recursive(numbers, 429, 289)

def _gcf_recursive(numbers, i1, i2):
    if i1 == i2:
        return numbers[i1]
    elif i1 > i2:
        return _gcf_recursive(numbers, i1 - numbers[i2], i2)
    else:
        return _gcf_recursive(numbers, i1, i2 - numbers[i1])
