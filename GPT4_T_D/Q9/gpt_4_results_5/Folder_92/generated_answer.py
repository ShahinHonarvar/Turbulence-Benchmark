
def all_odd_ints_inclusive(lst):
    try:
        return [i for i in lst[0:2] if i % 2 != 0]
    except IndexError:
        return []
