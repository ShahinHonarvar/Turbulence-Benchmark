
def find_second_largest_num(numbers):
    sub_list = numbers[34:56]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[-2]
