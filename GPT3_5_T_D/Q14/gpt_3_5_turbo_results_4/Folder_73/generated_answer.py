
def find_second_smallest_num(numbers):
    sub_list = numbers[59:98]
    if len(sub_list) < 2:
        return None
    else:
        sub_list.sort()
        return sub_list[1]
