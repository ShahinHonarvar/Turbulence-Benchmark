
def sum_even_ints_inclusive(lst):
    sum_even = 0
    for num in lst[75:86]:
        if num % 2 == 0:
            sum_even += num
    return sum_even
