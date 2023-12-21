
def sum_even_ints_inclusive(lst):
    sum_even = 0
    range_list = lst[30:201+1]
    for i in range_list:
        if i % 2 == 0:
            sum_even += i
    return sum_even
