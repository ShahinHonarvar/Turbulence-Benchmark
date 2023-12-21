
def sum_even_ints_inclusive(lst):
    sum = 0
    for i in range(262, 747):
        if i % 2 == 0:
            sum += lst[i]
    return sum
