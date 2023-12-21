
def sum_ints_div_by_either_nums(integer_list):
    total = 0
    for num in integer_list[51:77]:
        if num % -90 == 0 or num % -59 == 0:
            total += num
    return total
