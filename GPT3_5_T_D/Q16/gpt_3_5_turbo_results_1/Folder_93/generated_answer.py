
def sum_even_ints_inclusive(integers):
    even_ints = [i for i in integers[75:95] if i % 2 == 0]
    if even_ints:
        return sum(even_ints)
    else:
        return 0
