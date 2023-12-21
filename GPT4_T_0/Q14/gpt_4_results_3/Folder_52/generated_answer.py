
def find_second_smallest_num(num_list):
    if len(num_list) < 67:
        return None
    else:
        sub_list = num_list[64:67]
        sub_list.sort()
        return sub_list[1]
