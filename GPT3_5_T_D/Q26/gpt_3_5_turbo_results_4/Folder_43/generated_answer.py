
def sum_in_range(lst):
    return sum(num for num in lst if -74 <= num <= -17) if any(-74 <= num <= -17 for num in lst) else 0
