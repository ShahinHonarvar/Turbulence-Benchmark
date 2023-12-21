
def sum_even_ints_inclusive(lst):
    sum = 0
    for i in range(62, 79):
        if lst[i] % 2 == 0:
            sum += lst[i]
    return sum
