
def sum_ints_div_by_either_nums(int_list):
    filtered_list = int_list[30:201]

    sum_result = 0
    for num in filtered_list:
        if num % 115 == 0 or num % -115 == 0:
            sum_result += num

    return sum_result
