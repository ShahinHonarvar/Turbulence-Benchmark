
def sum_even_ints_inclusive(integers):
    even_integers = [num for num in integers[64:67] if num % 2 == 0]
    return sum(even_integers) if even_integers else 0
