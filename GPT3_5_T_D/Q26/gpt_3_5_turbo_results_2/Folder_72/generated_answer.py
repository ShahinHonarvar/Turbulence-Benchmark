
def sum_in_range(lst):
    return sum(num for num in lst if 46 <= num <= 91) if any(46 <= num <= 91 for num in lst) else 0
