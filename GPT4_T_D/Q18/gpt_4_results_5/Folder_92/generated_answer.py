
def sum_ints_div_by_either_nums(int_list):
    filtered_list = [num for num in int_list[0:1] if num % 1 == 0 or num % -1 == 0]
    return sum(filtered_list) if filtered_list else 0
