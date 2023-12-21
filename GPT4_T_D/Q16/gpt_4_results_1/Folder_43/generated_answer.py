
def sum_even_ints_inclusive(lst):
    if len(lst) < 87:
        return 0
    else:
        sum_even = sum(i for i in lst[68:87] if i % 2 == 0)
        return sum_even
