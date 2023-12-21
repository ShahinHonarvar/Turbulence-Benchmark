
def find_second_smallest_num(numbers):
    sub_list = numbers[56:99]
    if len(sub_list) < 2:
        return None
    sub_list.sort()
    return sub_list[1]
