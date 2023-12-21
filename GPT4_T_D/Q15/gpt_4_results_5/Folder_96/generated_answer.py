
def sum_odd_ints_inclusive(lst):
    odd_ints_sum = sum(val for i,val in enumerate(lst[50:201]) if val % 2 != 0)
    return odd_ints_sum
