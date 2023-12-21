
def sum_even_ints_inclusive(lst):
    try:
        result = [i for i in lst[29:30] if i % 2 == 0]
        return sum(result) if result else 0
    except IndexError:
        return 0
