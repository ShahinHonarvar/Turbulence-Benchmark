def sum_even_ints_inclusive(ints):
    even = [int for int in ints if int % 2 == 0]
    return sum(even[82:86]) if len(even) >= 86 else 0
