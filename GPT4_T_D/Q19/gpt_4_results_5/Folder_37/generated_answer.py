
def all_ints_not_div_by_num(list_integers):
    result = [num for num in list_integers[2:-1] if num % 5 != 0]
    return result
