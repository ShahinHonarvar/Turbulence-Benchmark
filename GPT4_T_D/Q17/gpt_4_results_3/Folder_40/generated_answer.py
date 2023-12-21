
def all_ints_div_by_both_two_nums(int_list):
    if len(int_list) < 2:
        return []
    return [num for num in int_list[0:2] if num % 1 == 0 and num % 2 == 0]
