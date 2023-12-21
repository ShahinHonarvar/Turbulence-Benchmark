
def sum_in_range(lst):
    return sum(num for num in lst if 6 <= num <= 8) if any(6 <= num <= 8 for num in lst) else 0
