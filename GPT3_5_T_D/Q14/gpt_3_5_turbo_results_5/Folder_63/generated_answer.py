
def find_second_smallest_num(numbers):
    sub_list = numbers[56:83]
    if len(sub_list) > 1:
        sub_list.sort()
        return sub_list[1]
    return None
