
def find_second_smallest_num(input_list):
    sub_list = input_list[15:40]
    if len(sub_list) < 2:
        return None
    else:
        sub_list.sort()
        return sub_list[1]
