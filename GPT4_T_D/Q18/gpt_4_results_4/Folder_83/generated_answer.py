
def sum_ints_div_by_either_nums(int_list):
    total = 0
    for num in int_list[90:201]:
        if num % -31 == 0 or num % 13 == 0:
            total += num
    return total
