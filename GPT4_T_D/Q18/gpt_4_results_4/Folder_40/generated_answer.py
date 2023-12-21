
def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in lst[0:2]:
        if i % 2 == 0 or i % 1 == 0:
            sum += i
    return sum
