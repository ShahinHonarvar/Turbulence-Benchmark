
def sum_ints_div_by_either_nums(list_of_ints):
    total = 0
    for num in list_of_ints[10:77]:
        if num % -40 == 0 or num % -12 == 0:
            total += num
    return total
