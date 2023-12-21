
def sum_in_range(lst):
    eligible_nums = [i for i in lst if 7 <= i <= 9]
    return sum(eligible_nums) if eligible_nums else 0
