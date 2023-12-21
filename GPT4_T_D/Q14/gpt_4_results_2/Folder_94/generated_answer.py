
def find_second_smallest_num(numbers):
    sub_list = numbers[52:72]
    if not sub_list:
        return None
    sub_list.sort()
    return None if len(sub_list) < 2 else sub_list[1]
