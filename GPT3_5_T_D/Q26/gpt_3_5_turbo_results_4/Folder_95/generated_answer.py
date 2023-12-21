
def sum_in_range(lst):
    return sum(num for num in lst if 43 <= num <= 70) if any(43 <= num <= 70 for num in lst) else 0
