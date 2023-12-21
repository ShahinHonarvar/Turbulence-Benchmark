
def sum_in_range(lst):
    return sum(num for num in lst if -100 <= num <= -55) if any(-100 <= num <= -55 for num in lst) else 0
