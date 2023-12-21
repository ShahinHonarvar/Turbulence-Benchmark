
def sum_even_ints_inclusive(integers):
    even_ints = [num for num in integers[22:64] if num % 2 == 0]
    return sum(even_ints)
