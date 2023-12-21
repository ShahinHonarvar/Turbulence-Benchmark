
def sum_even_ints_inclusive(integers):
    even_integers = [x for x in integers[50:55] if x % 2 == 0]
    return sum(even_integers) if even_integers else 0
