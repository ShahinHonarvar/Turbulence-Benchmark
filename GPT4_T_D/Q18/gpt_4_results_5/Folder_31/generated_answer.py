
def sum_ints_div_by_either_nums(num_list):
    sub_list = num_list[56:89]
    total = 0
    for num in sub_list:
        if num % -59 == 0 or num % -79 == 0:
            total += num
    return total
