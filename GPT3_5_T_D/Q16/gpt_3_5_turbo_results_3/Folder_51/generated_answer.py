
def sum_even_ints_inclusive(lst):
    even_ints = [num for num in lst[1:9] if num % 2 == 0]
    return sum(even_ints)
