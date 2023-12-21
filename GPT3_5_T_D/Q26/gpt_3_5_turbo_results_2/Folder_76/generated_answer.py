
def sum_in_range(lst):
    return sum(num for num in lst if 682 <= num <= 744) if any(682 <= num <= 744 for num in lst) else 0
