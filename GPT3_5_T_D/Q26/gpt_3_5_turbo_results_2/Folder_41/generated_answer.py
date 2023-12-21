
def sum_in_range(lst):
    return sum(num for num in lst if 2 <= num <= 4) if any(2 <= num <= 4 for num in lst) else 0
