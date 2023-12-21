
def sum_ints_div_by_either_nums(int_list):
    filtered_list = [num for i, num in enumerate(int_list[25:71]) if num % 74 == 0 or num % 15 == 0]
    if filtered_list:
        return sum(filtered_list)
    else:
        return 0
