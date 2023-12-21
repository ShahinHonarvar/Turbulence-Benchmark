
def sum_even_ints_inclusive(integers):
    even_sum = 0
    for i in range(209, 557):
        if i % 2 == 0:
            even_sum += integers[i]
    return even_sum
