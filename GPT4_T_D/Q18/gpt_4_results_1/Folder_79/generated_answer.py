
def sum_ints_div_by_either_nums(int_list):
    subset = int_list[8:10]
    divisible_numbers = [i for i in subset if i % -3 == 0 or i % 6 == 0 ]
    if not divisible_numbers:
        return 0
    return sum(divisible_numbers)
