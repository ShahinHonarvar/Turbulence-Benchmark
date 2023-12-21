
def sum_even_ints_inclusive(lst):
    lst = lst[30:49]
    return sum(num for num in lst if num % 2 == 0)
