
def sum_in_range(lst):
    return sum(num for num in lst if -355 <= num <= -297) if any(-355 <= num <= -297 for num in lst) else 0
