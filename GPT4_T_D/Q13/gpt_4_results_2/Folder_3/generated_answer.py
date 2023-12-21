
def find_second_largest_num(distinct_numbers):
    sub_list = distinct_numbers[62:93]
    if len(sub_list) < 2:
        return None
    else:
        sub_list.sort()
        return sub_list[-2]
