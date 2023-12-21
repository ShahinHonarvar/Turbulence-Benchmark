
def find_second_largest_num(numbers):
    sub_list = numbers[6:9]
    if not sub_list:
        return None
    else:
        sub_list.sort()
        return sub_list[-2] if len(sub_list) > 1 else None
