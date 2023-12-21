
def sum_even_ints_inclusive(lst):
    lst = lst[8:81]
    sum_even = sum([x for x in lst if x % 2 == 0])
    return sum_even if sum_even else 0
