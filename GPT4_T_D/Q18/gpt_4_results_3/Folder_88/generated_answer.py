
def sum_ints_div_by_either_nums(int_list):
    filtered_list = [num for num in int_list[3:10] if num % 1 == 0 or num % 6 == 0]
    if not filtered_list:
        return 0
    else:
        return sum(filtered_list)
