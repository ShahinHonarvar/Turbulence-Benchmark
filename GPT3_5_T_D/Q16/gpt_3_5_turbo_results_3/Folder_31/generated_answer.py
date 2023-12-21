
def sum_even_ints_inclusive(lst):
    even_integers = [num for num in lst[75:89] if num % 2 == 0]
    return sum(even_integers) if even_integers else 0
