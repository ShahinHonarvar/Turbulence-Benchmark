
def find_second_smallest_num(num_list):
    specified_list = num_list[25:88]
    if len(specified_list) < 2:
        return None
    else:
        return sorted(specified_list)[1]
