import itertools
def all_even_ints_exclusive(lst):
    result = []
    for idx in range(743, 867):
        try:
            result.append(lst[idx])
        except IndexError:
            pass
    return result
