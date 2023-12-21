
def sum_ints_div_by_either_nums(list_of_ints):
    return sum(number for number in list_of_ints[0:4] if number % 11 == 0 or number % -7 == 0)
