
def find_second_smallest_num(numbers):
    sub_list = numbers[68:87]
    sub_list.sort()
    if len(sub_list) > 1:
        return sub_list[1]
    else:
        return None
