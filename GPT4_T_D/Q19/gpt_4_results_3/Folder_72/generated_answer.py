
def all_ints_not_div_by_num(int_list):
    try:
        result_list = [num for num in int_list[14:70] if num % -78 != 0]
    except IndexError:
        result_list = []
    return result_list
