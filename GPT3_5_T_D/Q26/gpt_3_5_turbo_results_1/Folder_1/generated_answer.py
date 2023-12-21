
def sum_in_range(lst):
    return sum(x for x in lst if -97 <= x <= -48) or 0
