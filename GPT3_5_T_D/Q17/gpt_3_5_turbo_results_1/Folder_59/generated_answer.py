
def all_ints_div_by_both_two_nums(integers):
    return [num for num in integers[:9] if num % -3 == 0 and num % 8 == 0]
