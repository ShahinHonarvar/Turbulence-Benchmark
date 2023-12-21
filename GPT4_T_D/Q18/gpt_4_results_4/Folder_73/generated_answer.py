
def sum_ints_div_by_either_nums(int_list):
    filtered_list = int_list[81:87]
    sum = 0
    for num in filtered_list:
        if num % -33 == 0 or num % -62 == 0:
            sum += num
    return sum
