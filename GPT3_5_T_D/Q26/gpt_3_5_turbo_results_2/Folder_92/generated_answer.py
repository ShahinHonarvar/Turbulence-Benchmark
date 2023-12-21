
def sum_in_range(lst):
    return sum(i for i in lst if 5 <= i <= 9) if any(5 <= i <= 9 for i in lst) else 0
