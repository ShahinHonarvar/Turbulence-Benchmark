
def find_second_largest_num(numbers):
    sub_list = numbers[22:51]
    if len(sub_list) > 1:
        sub_list.sort()
        return sub_list[-2]
    else:
        return None
