
def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 201:
        return 0
    else:
        num = int_list[200]
        if num % 17 == 0 or num % -5 == 0:
            return num
        else:
            return 0
