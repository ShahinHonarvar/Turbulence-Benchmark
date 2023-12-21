
def sum_ints_div_by_either_nums(int_list):
    valid_nums = [num for num in int_list[54:80] if num % 54 == 0 or num % 28 == 0]
    return sum(valid_nums) if valid_nums else 0
