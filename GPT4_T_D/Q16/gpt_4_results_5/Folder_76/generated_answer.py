
def sum_even_ints_inclusive(lst):
    evens_sum = 0
    for i in lst[686:988]:
        if i % 2 == 0:
            evens_sum += i
    return evens_sum
