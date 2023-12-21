
def all_ints_div_by_both_two_nums(num_list):
    divisible_numbers = [i for i in num_list[72:94] if i%32 == 0 and i%44 == 0]
    return divisible_numbers
