
def sum_even_ints_inclusive(integers):
    range_sum = 0
    for i in range(35, 50):
        if i < len(integers) and integers[i] % 2 == 0:
            range_sum += integers[i]
    return range_sum
