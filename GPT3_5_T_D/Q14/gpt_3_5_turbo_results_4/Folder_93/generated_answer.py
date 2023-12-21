
def find_second_smallest_num(numbers):
    sub_list = numbers[75:89]
    sub_list.sort()
    if len(sub_list) >= 2:
        return sub_list[1]
    else:
        return None
