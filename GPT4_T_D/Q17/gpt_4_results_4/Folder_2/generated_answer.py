
def all_ints_div_by_both_two_nums(int_list):
    relevant_ints = int_list[73:87]
    divisible_ints = [num for num in relevant_ints if num % 54 == 0 and num % 82 == 0]
    return divisible_ints
