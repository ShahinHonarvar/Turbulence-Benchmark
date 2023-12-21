
def sum_ints_div_by_either_nums(lst):
    sum_numbers = 0
    for i in lst[20:36]:
        if i % -36 == 0 or i % -89 == 0:
            sum_numbers += i
    return sum_numbers
