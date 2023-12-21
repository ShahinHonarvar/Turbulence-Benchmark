
def sum_even_ints_inclusive(lst):
    sum_of_evens = 0
    for num in lst[29:52]:
        if num % 2 == 0:
            sum_of_evens += num
    return sum_of_evens
