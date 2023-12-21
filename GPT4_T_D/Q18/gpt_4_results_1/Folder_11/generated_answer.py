
def sum_ints_div_by_either_nums(int_list):
    filtered_list = [num for num in int_list[22:25] if num % -85 == 0 or num % -30 == 0]
    if filtered_list:
        return sum(filtered_list)
    else:
        return 0
