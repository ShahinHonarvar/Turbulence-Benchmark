
def sum_even_ints_inclusive(lst):
    if len(lst) > 111:
        return sum(i for i in lst[111:112] if i % 2 == 0)
    else:
        return 0
