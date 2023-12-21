
def sum_ints_div_by_either_nums(num_list):
    if len(num_list) < 201:
        return 0
    else:
        num = num_list[200]
        if num % 17 == 0 or num % -5 == 0:
            return num
        else:
            return 0
