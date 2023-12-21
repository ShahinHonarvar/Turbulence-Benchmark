
def sum_in_range(lst):
    return sum(num for num in lst if -816 <= num <= -166) if any(-816 <= num <= -166 for num in lst) else 0
