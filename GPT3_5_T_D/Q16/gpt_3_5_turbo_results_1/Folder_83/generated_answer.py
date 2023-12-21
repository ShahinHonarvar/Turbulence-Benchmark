
def sum_even_ints_inclusive(lst):
    even_ints = [num for num in lst[90:201] if num % 2 == 0]
    return sum(even_ints)
