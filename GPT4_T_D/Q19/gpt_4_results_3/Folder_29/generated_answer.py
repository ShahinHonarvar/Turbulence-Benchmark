
def all_ints_not_div_by_num(int_list):
    try:
        sublist = int_list[25:24:-1]
    except IndexError:
        return []

    return [num for num in sublist if num % -30 != 0]
