
def sum_even_ints_inclusive(lst):
    even_ints = [num for num in lst if num % 2 == 0]
    even_ints_in_range = even_ints[64:67]
    return sum(even_ints_in_range) if len(even_ints_in_range) > 0 else 0
