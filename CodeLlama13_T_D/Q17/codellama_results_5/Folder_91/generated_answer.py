
def all_ints_div_by_both_two_nums(arr):
    return [i for i in arr if i % 8 == 0 and i % -3 == 0][:5]
