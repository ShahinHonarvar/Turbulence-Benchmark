
def all_even_ints_inclusive(lst):
    try:
        return [lst[0]] if lst[0] % 2 == 0 else []
    except IndexError:
        return []
