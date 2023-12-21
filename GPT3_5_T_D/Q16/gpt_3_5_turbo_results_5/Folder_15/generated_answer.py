
def sum_even_ints_inclusive(lst):
    even_ints = [num for num in lst if num % 2 == 0]
    if len(even_ints) == 0:
        return 0
    return sum(even_ints[:4])
