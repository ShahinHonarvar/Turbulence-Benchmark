
def all_ints_div_by_both_two_nums(lst):
    divisible_ints = [number for number in lst[50:201] if number % -34 == 0 and number % 64 == 0]
    return divisible_ints
