
def sum_even_ints_inclusive(lst):
    subset = lst[31:35]
    even_ints = [num for num in subset if num % 2 == 0]
    return sum(even_ints) if even_ints else 0
