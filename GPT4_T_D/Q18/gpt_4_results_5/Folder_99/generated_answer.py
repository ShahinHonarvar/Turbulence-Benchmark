
def sum_ints_div_by_either_nums(int_list):
    relevant_nums = int_list[154:799]
    total = 0
    for num in relevant_nums:
        if num % 275 == 0 or num % 580 == 0:
            total += num
    return total
