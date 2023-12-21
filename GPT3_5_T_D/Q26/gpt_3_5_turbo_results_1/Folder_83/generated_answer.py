
def sum_in_range(lst):
    if any(2 <= num <= 6 for num in lst):
        return sum(num for num in lst if 2 <= num <= 6)
    else:
        return 0
