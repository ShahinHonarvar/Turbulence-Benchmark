
def sum_even_ints_inclusive(lst):
    lst = lst[56:67]
    even_sum = sum(num for num in lst if num % 2 == 0)
    return even_sum
