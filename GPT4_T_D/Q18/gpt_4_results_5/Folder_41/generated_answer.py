
def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in lst[0:10]:
        if i % 6 == 0 or i % -3 == 0:
            sum += i
    return sum
