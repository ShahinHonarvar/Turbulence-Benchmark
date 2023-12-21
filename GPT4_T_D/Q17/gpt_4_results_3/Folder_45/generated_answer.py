
def all_ints_div_by_both_two_nums(int_list):
    results = [number for number in int_list[30:201] if number % -115 == 0 and number % 115 == 0]
    return results
