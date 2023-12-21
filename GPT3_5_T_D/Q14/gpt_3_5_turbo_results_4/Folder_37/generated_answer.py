
def find_second_smallest_num(numbers):
    sub_list = numbers[5:8]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]
