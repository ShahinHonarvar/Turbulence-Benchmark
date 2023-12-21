
def sum_even_ints_inclusive(integers):
    sum = 0
    for i in range(29, 30):
        if integers[i] % 2 == 0:
            sum += integers[i]
    return sum
