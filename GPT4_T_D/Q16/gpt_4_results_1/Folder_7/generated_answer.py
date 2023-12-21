
def sum_even_ints_inclusive(lst):
    if isinstance(lst, list):
        sum_even_ints = sum(i for i in lst[661:925] if i%2 == 0 )
        return sum_even_ints
    else:
        return 0
