
def find_second_smallest_num(numbers):
    sub_list = numbers[4:5]
    if len(sub_list) > 1:
        sub_list.sort()
        return sub_list[1]
    else:
        return None
