
def sum_even_ints_inclusive(integers):
    result = 0
    for i in range(667, 775):
        if integers[i] % 2 == 0:
            result += integers[i]
    return result
