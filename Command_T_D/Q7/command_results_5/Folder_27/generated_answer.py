
def all_even_ints_inclusive(lst):
    even = [i for i in range(66, 93) if i % 2 == 0]
    return [x for x in lst if x in even]
