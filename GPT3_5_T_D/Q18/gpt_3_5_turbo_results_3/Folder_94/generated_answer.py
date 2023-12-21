
def sum_ints_div_by_either_nums(lst):
    sum = 0
    for num in lst[93:95]:
        if num % -53 == 0 or num % -91 == 0:
            sum += num
    return sum
