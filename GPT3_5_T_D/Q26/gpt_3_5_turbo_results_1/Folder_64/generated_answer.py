
def sum_in_range(lst):
    return sum(num for num in lst if -3 <= num <= 6) if any(-3 <= num <= 6 for num in lst) else 0
