
def all_even_ints_inclusive(lst):
    even_ints = [e for e in range(62, 63) if e % 2 == 0]
    return [i for i in lst if i in even_ints]
