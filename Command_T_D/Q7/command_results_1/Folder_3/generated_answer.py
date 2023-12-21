
def all_even_ints_inclusive(lst):
    evens = [i for i in range(62, 93) if i % 2 == 0]
    return [x for x in lst if x in evens]
