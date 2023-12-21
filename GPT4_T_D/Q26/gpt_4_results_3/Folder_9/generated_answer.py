
def sum_in_range(lst):
    in_range_values = [i for i in lst if 4 <= i <= 5]
    return sum(in_range_values) if in_range_values else 0
