
def all_ints_div_by_both_two_nums(num_list):
    divisible_ints = [num for num in num_list[306:958] if num % 982 == 0 and num % 319 == 0]
    return divisible_ints
