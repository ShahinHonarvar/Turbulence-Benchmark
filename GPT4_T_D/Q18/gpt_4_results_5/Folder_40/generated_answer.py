
def sum_ints_div_by_either_nums(lst):
    sublist = lst[:2]
    sum = 0
    for i in sublist:
        if i % 2 == 0 or i % 1 == 0:
            sum += i
    return sum
