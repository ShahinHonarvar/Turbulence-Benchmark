
def sum_even_ints_inclusive(lst):
    if len(lst) >= 79:
        return sum([n for n in lst[17:79] if n % 2 == 0])
    elif len(lst) > 17:
        return sum([n for n in lst[17:] if n % 2 == 0])
    else:
        return 0
