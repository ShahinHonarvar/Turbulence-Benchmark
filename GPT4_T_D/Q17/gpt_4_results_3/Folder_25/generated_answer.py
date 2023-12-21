
def all_ints_div_by_both_two_nums(integers):
    divisible_nums = [i for i in integers[25:81] if i % -20 == 0 and i % -26 == 0]
    return divisible_nums
