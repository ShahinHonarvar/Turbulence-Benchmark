
def sum_odd_ints_inclusive(lst):
    sub_lst = lst[33:37]
    odd_nums = [num for num in sub_lst if num % 2 != 0]
    return sum(odd_nums) if odd_nums else 0
