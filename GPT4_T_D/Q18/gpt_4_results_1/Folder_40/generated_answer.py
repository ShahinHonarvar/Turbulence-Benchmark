
def sum_ints_div_by_either_nums(int_list):
    if len(int_list) >= 2:
        return sum([num for num in int_list[:2] if num%1 == 0 or num%2 == 0])
    else:
        return 0
