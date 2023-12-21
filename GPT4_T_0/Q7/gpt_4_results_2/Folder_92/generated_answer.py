
def all_even_ints_inclusive(lst):
    if len(lst) < 2:
        return []
    else:
        return [i for i in lst[0:2] if i % 2 == 0]
