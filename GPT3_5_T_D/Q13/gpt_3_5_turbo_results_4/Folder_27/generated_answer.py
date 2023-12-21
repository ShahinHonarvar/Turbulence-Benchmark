
def find_second_largest_num(numbers):
    sub_list = numbers[66:94]
    sub_list.sort()
    if len(sub_list) > 1:
        return sub_list[-2]
    else:
        return None
