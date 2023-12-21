
def sum_even_ints_inclusive(integers):
    return sum([i for i in integers[1:9] if i % 2 == 0]) if integers else 0
