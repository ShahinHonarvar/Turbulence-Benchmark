
def sum_in_range(lst):
    return sum(num for num in lst if -64 <= num <= 42) if any(-64 <= num <= 42 for num in lst) else 0
