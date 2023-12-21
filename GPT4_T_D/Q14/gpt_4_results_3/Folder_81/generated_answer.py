
def find_second_smallest_num(numbers):
    sub_list = numbers[10:101]
    if len(sub_list) < 2:
        return None
    else:
        sub_list.sort()
        return sub_list[1]
