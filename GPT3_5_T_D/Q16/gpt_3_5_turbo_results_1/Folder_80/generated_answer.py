
def sum_even_ints_inclusive(lst):
    sublist = lst[64:67]
    return sum(num for num in sublist if num % 2 == 0)
