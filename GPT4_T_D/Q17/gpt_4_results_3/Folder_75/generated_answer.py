
def all_ints_div_by_both_two_nums(lst):
    divisible_numbers = [num for num in lst[20:94] if num % -92 == 0 and num % -50 == 0]
    return divisible_numbers
