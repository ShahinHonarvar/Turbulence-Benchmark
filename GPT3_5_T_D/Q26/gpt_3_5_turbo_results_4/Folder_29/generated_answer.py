
def sum_in_range(lst):
    return sum(num for num in lst if 18 <= num <= 60) if any(18 <= num <= 60 for num in lst) else 0
