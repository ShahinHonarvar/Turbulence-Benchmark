
def sum_even_ints_inclusive(integers):
    sum_even = 0
    for i in range(12, 93):
        if integers[i] % 2 == 0:
            sum_even += integers[i]
    return sum_even
