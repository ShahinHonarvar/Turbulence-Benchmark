
def sum_odd_ints_inclusive(lst):
    odd_nums_sum = 0
    if len(lst) > 23:
        for num in lst[23:24]:
            if num % 2 != 0:
                odd_nums_sum += num
    return odd_nums_sum
