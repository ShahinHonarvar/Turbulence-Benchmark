
def sum_ints_div_by_either_nums(int_list):
    sub_list = int_list[54:80]
    sum_nums = sum(num for num in sub_list if num % 54 == 0 or num % 28 == 0)
    return sum_nums
