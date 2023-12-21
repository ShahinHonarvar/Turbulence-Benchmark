
def sum_even_ints_inclusive(integers):
    even_integers = [i for i in integers[56:99] if i % 2 == 0]
    return sum(even_integers) if even_integers else 0
