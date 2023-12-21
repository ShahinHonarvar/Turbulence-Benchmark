
def sum_even_ints_inclusive(integers):
    even_sum = 0
    for index in range(8, 10):
        if integers[index] % 2 == 0:
            even_sum += integers[index]
    return even_sum
