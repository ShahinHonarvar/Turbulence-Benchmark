
def sum_even_ints_inclusive(lst):
    sum_even = 0
    for n in lst[75:95]:
        if n % 2 == 0:
            sum_even += n
    return sum_even
