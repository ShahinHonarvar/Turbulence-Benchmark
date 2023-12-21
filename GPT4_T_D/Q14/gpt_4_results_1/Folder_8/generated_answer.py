
def find_second_smallest_num(num_list):
    sub_list = num_list[56:67]
    if len(sub_list)<2:
        return None
    else:
        sub_list.sort()
        return sub_list[1]
