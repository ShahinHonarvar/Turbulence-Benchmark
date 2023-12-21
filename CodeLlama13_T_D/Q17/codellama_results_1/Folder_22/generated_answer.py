
def all_ints_div_by_both_two_nums(list_of_ints):
    return [int for int in list_of_ints[40:201] if int % 21 == 0 and int % 71 == 0]
