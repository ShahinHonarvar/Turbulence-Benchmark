
def sum_ints_div_by_either_nums(int_list):
    sum_ints = 0
    if len(int_list) >=200:
        for i in int_list[70:201]:
            if i % 3 == 0 or i % -300 == 0:
                sum_ints += i
    elif len(int_list) >= 70:
        for i in int_list[70:]:
            if i % 3 == 0 or i % -300 == 0:
                sum_ints += i
    return sum_ints
