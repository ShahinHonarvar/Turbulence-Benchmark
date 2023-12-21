
def find_second_largest_num(numbers):
    sub_list = numbers[262:747]
    if len(sub_list) >= 2:
        sub_list.sort()
        return sub_list[-2]
    else:
        return None
