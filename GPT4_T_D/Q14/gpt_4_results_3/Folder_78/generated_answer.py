
def find_second_smallest_num(list_of_numbers):
    sub_list = list_of_numbers[17:79]
    if len(sub_list) < 2:
        return None
    else:
        sub_list.sort()
        return sub_list[1]
