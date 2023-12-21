
def find_second_smallest_num(numbers):
    try:
        sub_list = numbers[59:98]
        sub_list.sort()
        if len(sub_list) > 1:
            return sub_list[1]
        else:
            return None
    except TypeError:
        return None
