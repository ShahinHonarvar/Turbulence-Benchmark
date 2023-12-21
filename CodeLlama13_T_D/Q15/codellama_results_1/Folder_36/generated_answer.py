
def sum_odd_ints_inclusive(lst):
    return sum([num for i, num in enumerate(lst[246:751]) if i % 2 == 0])
