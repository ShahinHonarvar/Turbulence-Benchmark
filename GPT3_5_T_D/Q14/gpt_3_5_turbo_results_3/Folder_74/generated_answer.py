
def find_second_smallest_num(numbers):
    sub_list = numbers[36:47]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    else:
        return sub_list[1]
