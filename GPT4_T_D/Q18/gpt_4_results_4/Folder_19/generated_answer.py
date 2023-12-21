
def sum_ints_div_by_either_nums(int_list):
    sub_list = int_list[1:5]
    total_sum = 0
    for num in sub_list:
        if num % 4 == 0 or num % -6 == 0:
            total_sum += num
            
    return total_sum
