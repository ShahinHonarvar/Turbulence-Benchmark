def sum_even_ints_inclusive(ints):
    even_ints = [int for int in ints if int % 2 == 0]
    if len(even_ints) == 0:
        return 0
    return sum(even_ints[40:80])
