
def all_ints_div_by_both_two_nums(list_of_ints):
    divisible_ints = [num for num in list_of_ints[0:3] if num % -2 == 0 and num % 3 == 0]
    return divisible_ints
