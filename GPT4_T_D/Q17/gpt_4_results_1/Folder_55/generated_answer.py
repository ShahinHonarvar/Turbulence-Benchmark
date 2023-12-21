
def all_ints_div_by_both_two_nums(int_list):
    result = [num for num in int_list[0:10] if num % 10 == 0 and num % 100 == 0]
    return result
