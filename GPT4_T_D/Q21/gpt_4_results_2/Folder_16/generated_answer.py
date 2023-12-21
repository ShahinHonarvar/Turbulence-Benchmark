
def all_ints_div_by_num(list_of_integers):
    divisible_by_71 = [number for number in list_of_integers[13:69] if number % 71 == 0]
    return divisible_by_71
