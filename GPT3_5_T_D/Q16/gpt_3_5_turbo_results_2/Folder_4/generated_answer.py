
def sum_even_ints_inclusive(lst):
    sum = 0
    for i in range(12, 93):
        if lst[i] % 2 == 0:
            sum += lst[i]
    return sum
